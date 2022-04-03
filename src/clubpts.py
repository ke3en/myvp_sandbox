#!/usr/bin/env python
# -*- coding: utf-8 -*-

def calc_club_pts(
        importance_coefficient: int,
        target_club_pts: int,
        opponent_club_pts: int,
        target_goals: int,
        opponent_goals: int,
        pk_win: bool = False,
) -> int:
    """クラブポイントを計算する関数.
    試合の重要度係数 (A) × (試合の結果係数(B) - 試合の期待結果係数(C) )

    :param importance_coefficient: 試合の重要度係数
    :param target_club_pts: 計算対象のチームの試合前のクラブポイント
    :param opponent_club_pts: 相手チームの試合前のクラブポイント
    :param target_goals: 計算対象のチームのゴール数
    :param opponent_goals: 相手チームのゴール数
    :param pk_win: 計算対象のチームがPK戦で勝利
    :returns: クラブポイント
    """
    if target_goals > opponent_goals:
        b = 1  # 通常勝利
    elif target_goals < opponent_goals:
        b = 0  # 負け
    elif pk_win:
        b = 0.75  # PK戦勝利
    else:
        b = 0.5  # 引分、PK負け
    c = calc_prediction(
        target_club_pts=target_club_pts,
        opponent_club_pts=opponent_club_pts,
    )
    delta = importance_coefficient * (b - c)
    return round(target_club_pts + delta)


def calc_prediction(
        target_club_pts: int,
        opponent_club_pts: int,
) -> float:
    """勝敗予想.

    :param target_club_pts: 計算対象のチームのクラブポイント
    :param opponent_club_pts: 相手チームのクラブポイント
    :return: 計算対象チームの勝率
    """
    d = opponent_club_pts - target_club_pts
    return 1 / (10 ** (d / 600) + 1)


if __name__ == '__main__':
    hone_club_p = calc_club_pts(50, 1400, 1300, 0, 1)
    away_club_p = calc_club_pts(50, 1300, 1400, 1, 0)

    home_club_pre = calc_prediction(1400, 1300)
    away_club_pre = calc_prediction(1300, 1400)

    print(hone_club_p)
    print(away_club_p)
    print(home_club_pre)
    print(away_club_pre)
