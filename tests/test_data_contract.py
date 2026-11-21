import csv
import io
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FIELDS = {'invites': ['invite', 'person', 'service', 'period', 'form', 'contact', 'status'], 'answers': ['invite', 'item', 'score', 'at'], 'anchors': ['service', 'old_form', 'new_form', 'dimension', 'old_item', 'new_item'], 'bridge': ['id', 'person', 'service', 'old_item', 'new_item', 'old_score', 'new_score', 'days', 'intervening_service', 'void_at'], 'bridge_policy': ['service', 'min_pairs', 'window_days', 'max_abs_mean_diff', 'max_opposite_share'], 'review_policy': ['service', 'dimension', 'drop', 'min_response', 'contact_slots'], 'service_events': ['invite', 'fact', 'at'], 'review_log': ['id', 'service', 'period', 'state', 'at', 'evidence']}


class DataContractTests(unittest.TestCase):
    def test_readable_source_tables(self):
        for name, fields in FIELDS.items():
            with self.subTest(table=name):
                text = (ROOT / 'data' / (name + '.csv')).read_text(encoding='utf-8')
                with io.StringIO(text, newline='') as stream:
                    reader = csv.reader(stream, strict=True)
                    self.assertEqual(next(reader), fields)
                    rows = list(reader)
                self.assertTrue(rows)
                self.assertTrue(all(len(row) == len(fields) for row in rows))
