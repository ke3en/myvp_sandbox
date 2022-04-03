def calc_club_pts(
        importance_coefficient: int,
        home_club_pts: int,
        away_club_pts: int,
        home_goals: int,
        away_goals: int,
        results: int,
        home_club_pts_after: int,
        away_club_pts_after: int,
) -> tuple[int, int]:
    """クラブポイントを計算する関数.
    試合の重要度係数 (A) × (試合の結果係数(B) - 試合の期待結果係数(C) )

    :param home_club_pts: ホームチームの試合前のクラブポイント
    :param away_club_pts: アウェイチームの試合前のクラブポイント
    :param home_goals: ホームチームのゴール数
    :param away_goals: アウェイチームのゴール数
    :param results: 1 -> ホームの勝ち, -1 -> アウェイの勝ち, 0 -> 引き分け
    :returns: 両チームのクラブポイント
    """

    # 勝利係数
    win_coefficient = 1  # 通常勝利
    win_coefficient2 = 0.75  # PK戦勝利
    draw_pkloss_coefficient = 0.5  # 引分、PK負け
    loss_coefficient = 0

    # ホーム計算
    home_a = importance_coefficient

    if home_goals > away_goals:
        home_b = win_coefficient
    elif home_goals == away_goals:
        home_b = draw_pkloss_coefficient
    else:
        home_b = loss_coefficient

    home_d = away_club_pts - home_club_pts

    home_c = 1 / (10 ** (home_d / 600) + 1)

    home_club_pts_after_buf = \
        home_a * (home_b - home_c)

    home_club_pts_after = round(home_club_pts + home_club_pts_after_buf)

    # アウェイ計算
    away_a = importance_coefficient

    if away_goals > home_goals:
        away_b = win_coefficient
    elif away_goals == home_goals:
        away_b = draw_pkloss_coefficient
    else:
        away_b = loss_coefficient

    away_d = home_club_pts - away_club_pts

    away_c = 1 / (10 ** (away_d / 600) + 1)

    away_club_pts_after_buf = \
        away_a * (away_b - away_c)

    away_club_pts_after = round(away_club_pts + away_club_pts_after_buf)

    return home_club_pts_after, away_club_pts_after


def calc_predection_winner(  # 勝敗予想
        home_club_pts: int,
        away_club_pts: int,
        home_predection,
        away_predection
) -> tuple[int, int]:
    home_d = away_club_pts - home_club_pts
    home_predection = round((1 / (10 ** (home_d / 600) + 1)), 2) * 100

    away_d = home_club_pts - away_club_pts
    away_predection = round((1 / (10 ** (away_d / 600) + 1)), 2) * 100

    return home_predection, away_predection


club_p = calc_club_pts(50, 1400, 1300, 0, 1, 0, 0, 0)
club_pre = calc_predection_winner(1400, 1300, 0, 0)
print(club_p)
print(club_pre)