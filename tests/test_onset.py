#!/usr/bin/env pytest

import onset

from hypothesis import HealthCheck, assume, given, settings, strategies
from hypothesis.stateful import RuleBasedStateMachine, invariant, rule

# specific strategy for tests
intset = strategies.sets(strategies.integers())


@given(intset)
def test_union_with_empty(s):
    s_ = s.copy()
    onset.union(s_, set())

    assert s_ == s


@given(intset)
def test_union_with_self(s):
    s_ = s.copy()
    onset.union(s_, s)

    assert s_ == s


@settings(suppress_health_check=[HealthCheck.filter_too_much])
@given(intset, intset)
def test_union_with_subset(s, t):
    assume(s.issubset(t))

    s_ = s.copy()
    onset.union(s_, t)

    assert s_ == t


@given(intset, intset)
def test_union_is_superset(s, t):
    s_ = s.copy()
    onset.union(s_, t)

    assert s_.issuperset(s)


@given(intset, intset)
def test_union_is_commutative(s, t):
    s_ = s.copy()
    t_ = t.copy()
    onset.union(s_, t)
    onset.union(t_, s)

    assert s_ == t_


@given(intset, intset, intset)
def test_union_is_associative(s, t, r):
    s_ = s.copy()
    t_ = t.copy()

    # (s U t) U r
    onset.union(s_, t)
    onset.union(s_, r)

    # s U (t U r)
    onset.union(t_, r)
    onset.union(t_, s)

    assert s_ == t_


@given(intset)
def test_difference_on_empty(s):
    t_ = set()
    onset.difference(t_, s)

    assert t_ == set()


@given(intset)
def test_difference_with_empty(s):
    s_ = s.copy()
    onset.difference(s_, set())

    assert s_ == s


@given(intset)
def test_difference_with_self(s):
    s_ = s.copy()
    onset.difference(s_, s)

    assert s_ == set()


@settings(suppress_health_check=[HealthCheck.filter_too_much])
@given(intset, intset)
def test_difference_with_subset(s, t):
    assume(s.issubset(t))

    s_ = s.copy()
    onset.difference(s_, t)

    assert s_ == set()


@given(intset, intset)
def test_difference_not_commutative(s, t):
    assume(s != t)

    s_ = s.copy()
    t_ = t.copy()
    onset.difference(s_, t)
    onset.difference(t_, s)

    assert s_ != t_


@given(intset)
def test_intersection_with_empty(s):
    s_ = s.copy()
    onset.intersection(s_, set())

    assert s_ == set()


@given(intset)
def test_intersection_with_self(s):
    s_ = s.copy()
    onset.intersection(s_, s)

    assert s_ == s


@settings(suppress_health_check=[HealthCheck.filter_too_much])
@given(intset, intset)
def test_intersection_with_subset(s, t):
    assume(s.issubset(t))

    s_ = s.copy()
    onset.intersection(s_, t)

    assert s_ == s


@given(intset, intset)
def test_intersection_is_subset(s, t):
    s_ = s.copy()
    onset.intersection(s_, t)

    assert s_.issubset(s)


@given(intset, intset)
def test_intersection_is_commutative(s, t):
    s_ = s.copy()
    t_ = t.copy()
    onset.intersection(s_, t)
    onset.intersection(t_, s)

    assert s_ == t_


@given(intset, intset, intset)
def test_intersection_is_associative(s, t, r):
    s_ = s.copy()
    t_ = t.copy()

    # (s I t) I r
    onset.intersection(s_, t)
    onset.intersection(s_, r)

    # s I (t I r)
    onset.intersection(t_, r)
    onset.intersection(t_, s)

    assert s_ == t_


@given(intset)
def test_disjunction_with_empty(s):
    s_ = s.copy()
    onset.disjunction(s_, set())

    assert s_ == s


@given(intset)
def test_disjunction_with_self(s):
    s_ = s.copy()
    onset.disjunction(s_, s)

    assert s_ == set()


@settings(suppress_health_check=[HealthCheck.filter_too_much])
@given(intset, intset)
def test_disjunction_with_subset(s, t):
    assume(s.issubset(t))

    s_ = s.copy()
    t_ = t.copy()
    onset.difference(t_, s)
    onset.disjunction(s_, t)

    assert s_ == t_


@given(intset, intset)
def test_disjunction_is_commutative(s, t):
    s_ = s.copy()
    t_ = t.copy()
    onset.disjunction(s_, t)
    onset.disjunction(t_, s)

    assert s_ == t_


@given(intset, intset, intset)
def test_disjunction_is_associative(s, t, r):
    s_ = s.copy()
    t_ = t.copy()

    # (s J t) J r
    onset.disjunction(s_, t)
    onset.disjunction(s_, r)

    # s J (t J r)
    onset.disjunction(t_, r)
    onset.disjunction(t_, s)

    assert s_ == t_


class OnSet(RuleBasedStateMachine):
    s = intset.example()

    @invariant()
    def is_set(self):
        assert isinstance(self.s, set)

    @rule(t=intset)
    def union(self, t):
        return onset.union(self.s, t)

    @rule(t=intset)
    def difference(self, t):
        return onset.difference(self.s, t)

    @rule(t=intset)
    def intersection(self, t):
        return onset.intersection(self.s, t)

    @rule(t=intset)
    def disjunction(self, t):
        return onset.disjunction(self.s, t)


TestOnSet = OnSet.TestCase
