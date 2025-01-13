
def test_cli():
    import subprocess
    output = subprocess.check_output(['mt-thresholds', 'bleu', '5']).decode('utf-8').strip()
    assert output == "87.635"
    output = subprocess.check_output(['mt-thresholds', 'xCometXXL', '5']).decode('utf-8').strip()
    assert output == "98.640"

def test_cli_delta():
    import subprocess
    output = subprocess.check_output(['mt-thresholds', 'bleu', '0.98', '--delta']).decode('utf-8').strip()
    assert output == "nan"
    output = subprocess.check_output(['mt-thresholds', 'xCometXXL', '0.98', '--delta']).decode('utf-8').strip()
    assert output == "4.001"


def test_python():
    import mt_thresholds
    assert abs(mt_thresholds.accuracy(5, 'bleu') - 87.635) < 0.001
    assert abs(mt_thresholds.accuracy(5, 'xcometxxl') - 98.640) < 0.001


def test_python_delta():
    import mt_thresholds
    import math
    assert math.isnan(mt_thresholds.delta(0.98, 'bleu'))
    assert abs(mt_thresholds.delta(0.98, 'xcometxxl') - 4.001) < 0.001