def calculate_risk(asset):

    score = 0

    score += len(
        asset["ports"]
    ) * 5

    score += len(
        asset["services"]
    ) * 3

    score += len(
        asset["technologies"]
    ) * 2

    score += len(
        asset["findings"]
    ) * 10

    if score > 100:

        score = 100

    return score
