def test_flush_empty(app, signalbus):
    runner = app.test_cli_runner()
    result = runner.invoke(args=['signalbus', 'flushmany'])
    assert not result.output


def test_flush_pending(app, signalbus_with_pending_signal, caplog):
    runner = app.test_cli_runner()
    runner.invoke(args=['signalbus', 'flushmany'])
    assert '1 signals have been successfully processed' in caplog.text


def test_flush_pending_explicit(app, signalbus_with_pending_signal, caplog):
    runner = app.test_cli_runner()
    runner.invoke(args=['signalbus', 'flushmany', 'Signal'])
    assert '1 signals have been successfully processed' in caplog.text
    assert "Started flushing Signal." in caplog.text


def test_flush_pending_explicit_wrong_name(
        app, signalbus_with_pending_signal, caplog):
    runner = app.test_cli_runner()
    result = runner.invoke(args=['signalbus', 'flushmany', 'WrongName'])
    result.exit_code == 0
    assert '1 signals have been successfully processed' not in caplog.text
    assert 'WARNING' in caplog.text
    assert 'A signal with name "WrongName" does not exist.' in caplog.text


def test_flush_error(app, signalbus_with_pending_error, caplog):
    runner = app.test_cli_runner()
    result = runner.invoke(args=['signalbus', 'flushmany'])
    assert isinstance(result.exception, SystemExit)
    assert 'error while sending pending signals' in caplog.text


def test_flushmany_nosignals(app, signalbus):
    runner = app.test_cli_runner()
    result = runner.invoke(args=['signalbus', 'flushmany'])
    assert not result.output


def test_flushmany_empty(app, signalbus, Signal):
    runner = app.test_cli_runner()
    result = runner.invoke(args=['signalbus', 'flushmany'])
    assert not result.output


def test_flushmany_pending(app, signalbus_with_pending_signal, caplog):
    runner = app.test_cli_runner()
    runner.invoke(args=['signalbus', 'flushmany'])
    assert "Started flushing Signal." in caplog.text
    assert '1 signals have been successfully processed' in caplog.text


def test_show_signals(app, signalbus_with_pending_signal):
    runner = app.test_cli_runner()
    result = runner.invoke(args=['signalbus', 'signals'])
    assert 'Signal' == result.output.strip()


def test_show_pending(app, signalbus_with_pending_signal):
    runner = app.test_cli_runner()
    result = runner.invoke(args=['signalbus', 'pending'])
    assert 'Signal' in result.output
    assert 'Total pending: 1' in result.output
