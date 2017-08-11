# Help GitHub feature branches "track" the main development branch

A tornado webapp for Heroko

Based on a fork of : https://github.com/pelson/my-first-heroku-tornado-app

The idea is to use webhooks to assist a "feature" development branch to track
changes on the related "main" branch.

It works with a given branch in a GitHub repository  
 -- this is currently *fixed* to https://github.com/pp-mo/github_trial.

A GitHub webhook (??type), is enabled to notify this app of changes.

Method:
-------

When a change is pushed to the default branch (e.g., typically, "master"),
then the app detects it and automatically raises a new PR to merge the default
into the tracking branch.  
This help to reduce drift between the feature and the main dev branch,
thus simplifying the eventual merge-back of the feature.

TODO:

 * support multiple branches / repos
 * have it serve a webpage where you can configure it
 * have it post config changes back to its own github repo (!)
