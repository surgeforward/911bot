# How to contribute

The 911bot project prides itself on solving a very specific problem. We love it
when people want to jump right in and get involved, so here is what you need to
know:

## Quick guide

1. Create or find an issue to address on
   our [issues page](https://github.com/surgeforward/911bot/issues).
2. Does your proposed
   change [fit 911bot's goals](#does-the-change-fit-911bots-goals)?
3. Fork the repository if you haven't done so already.
4. Make your changes in a new branch specifically for your chosen issue.
5. Test your changes. Include your tests as part of the PR.
6. Push to your fork, rebase your changes to a single commit and submit a pull
   request.

## Does the change fit 911bot's goals?

As a rough guideline, ask yourself the following questions to determine if your
proposed change fits the 911bot's project goals. Please remember that this is
only a rough guideline and may or may not reflect the definitive answer to this
question.

* Does it make the job of accessing emergency information in an emergency less
  prone to failure?
* Does it make the job of modifying your own emergency information easier?
* Does it make the stored or storing of information more secure?
* Does it eliminate technical debt?

If you answered yes to any of these questions, chances are high that your change
fits the project goals and will likely be accepted. Regardless, there are a few
other important questions you need to ask yourself before you start working on a
change:

* Is this change reasonably supportable and maintainable?
* Is this change tested?

## Making the changes

* Create a branch on your fork where you'll be making your changes
    * Name your branch something relevant. We recommend `<issue-id>-<short
      summary>`. For example `28-governance-docs`.
* Check for unnecessary whitespace before committing
* Make sure your author information is correct. Your PR will be rejected without
  proper author information
* Make sure your code meets [our requirements](#code-requirements).
* Test your changes to make sure it actually addresses the issue it should.
* Make sure your code runs under Python 2.7 (see #5)
* Rebase your commits to a single commit.

## Code requirements

For now, just make it look like the current codebase. This includes:

* A single space between functions
* Spaces, not tabs
* 4 spaces for block indent in Python
* A single import statement per line
* ["Why", not "how" comments](https://blog.codinghorror.com/code-tells-you-how-comments-tell-you-why/).

