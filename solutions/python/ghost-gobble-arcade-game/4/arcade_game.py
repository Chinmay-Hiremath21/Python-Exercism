"""Functions for implementing the rules of the classic arcade game Pac-Man."""

def eat_ghost(power_pellet_active, touching_ghost):
    """Return True when Pac-Man can eat a ghost.

    :param power_pellet_active: bool - does the player have an active power pellet?
    :param touching_ghost: bool - is the player touching a ghost?
    :return: bool - can a ghost be eaten?
    """
    return power_pellet_active and touching_ghost


def score(touching_power_pellet, touching_dot):
    """Return True if Pac-Man scored (ate a power pellet or a dot).

    :param touching_power_pellet: bool - is the player touching a power pellet?
    :param touching_dot: bool - is the player touching a dot?
    :return: bool - has the player scored?
    """
    return touching_power_pellet or touching_dot


def lose(power_pellet_active, touching_ghost):
    """Return True when Pac-Man loses (touches a ghost without an active power pellet).

    :param power_pellet_active: bool - does the player have an active power pellet?
    :param touching_ghost: bool - is the player touching a ghost?
    :return: bool - has the player lost the game?
    """
    return touching_ghost and not power_pellet_active


def win(has_eaten_all_dots, power_pellet_active, touching_ghost):
    """Return True when Pac-Man has won.

    Win happens when all dots are eaten **and** Pac-Man hasn't just lost by touching a ghost
    while the power pellet is inactive.

    :param has_eaten_all_dots: bool - has the player eaten all the dots?
    :param power_pellet_active: bool - does the player have an active power pellet?
    :param touching_ghost: bool - is the player touching a ghost?
    :return: bool - has the player won the game?
    """
    # Player wins only if all dots are eaten and they haven't lost at the same moment:
    # i.e., not (touching_ghost and not power_pellet_active)
    return has_eaten_all_dots and not (touching_ghost and not power_pellet_active)
