from sixfeetup.utils import helpers as sfutils


def importVarious(context):
    """Run the setup handlers for the default profile"""
    if context.readDataFile('pse12_initialcontent-default.txt') is None:
        return
    # automagically run the upgrade steps for this package
    sfutils.runUpgradeSteps(u'pse12.initialcontent:default')
