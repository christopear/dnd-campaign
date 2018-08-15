# dnd-campaign

This project is a WIP. The foundational thought process behind this project is to provide a toolset for simulating societies and people to provide a descriptive back drop to a Dungeons and Dragons campaign.

## Current progress


#### People

Manual planning for people is undertaken outside of github; however, the premise is to have a person represented by an object and contain all details within. Families will be generated and mapped out in future.

#### Races

The first steps so far have been in creating the people. Name generators have been scraped from [Fantasy Name Generators](http://fantasynamegenerators.com) for each individual class, converted from javascript and put into a working package structure.

Each race has been assigned its own class, inheriting from a broader set of classes that define standard name generation methods.

#### Life expectancy

Work has begun on creating the statistical methods for life expectancy. Adapting the Weibull distribution a distribution is implemented that calculates the scalar_survival rate (e.g. 100 people born, X many alive at 50 yo). This will be adapted to provide probabilities each year of death - allowing a more fluid way of calculating death age (rather than just pre-determining it).


## Future steps

Plans have been undertaken to figure out how to model families (e.g. with a seperate object or all internal to the person). Thought has also gone into power dynamics and economics.
