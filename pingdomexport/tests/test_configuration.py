import pytest
from pingdomexport import configuration

class TestPingdomAccess:
    def test_from_dict(self):
        config = configuration.PingdomAccess.from_dict(
            {
                "username": 'u',
                "password": 'p',
                "account_email": 'ae',
                "app_key": "akey"
            }
        )
        assert config.username() == 'u'
        assert config.password() == 'p'
        assert config.account_email() == 'ae'
        assert config.app_key() == 'akey'

    def test_from_dict_missing_key(self):
        with pytest.raises(KeyError):
            configuration.PingdomAccess.from_dict({})

class TestChecks:
    def test_strategy_unrecognized(self):
        with pytest.raises(ValueError):
            configuration.Checks('t', [])
    def test_strategty_all_with_ids(self):
        with pytest.raises(ValueError):
            configuration.Checks('all', [1,2])
    def test_from_dict_missing_key(self):
        with pytest.raises(KeyError):
            configuration.Checks.from_dict({})
    def test_is_strategy_all(self):
        checks = configuration.Checks('all', [])
        assert checks.is_strategy_all();
        checks = configuration.Checks('include', [])
        assert not checks.is_strategy_all();
    def test_is_strategy_include(self):
        checks = configuration.Checks('include', [123])
        assert checks.is_strategy_include();
        checks = configuration.Checks('all', [])
        assert not checks.is_strategy_include();
    def test_is_strategy_exclude(self):
        checks = configuration.Checks('exclude', [123])
        assert checks.is_strategy_exclude();
        checks = configuration.Checks('all', [])
        assert not checks.is_strategy_exclude();