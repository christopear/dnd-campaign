# dnd-campaign

This project is a WIP. The foundational thought process behind this project is to provide a toolset for simulating societies and people to provide a descriptive back drop to a Dungeons and Dragons campaign.

## Current progress


### People

Manual planning for people is undertaken outside of github; however, the premise is to have a person represented by an object and contain all details within. Families will be generated and mapped out in future.

##### Structure
Have settled on an class structure, where each race is a class (as opposed to race being a variable). This choice was made for future proofing purposes: in future, each race will have different random generation requirements (such as name, age, life expectancy, attraction, etc.) which is better dealt with using class inheritance.

Top level classes are abstract classes. Each race inherits from top level Race class, which defines some base characteristics (such as marriage rules).

##### Races

Name generators have been scraped from [Fantasy Name Generators](http://fantasynamegenerators.com) for each individual class, converted from javascript into pythonand put into a working package structure. They have also been classified into their lore origin (e.g. core 5e, UA, volo, etc.) - development will mainly focus on the Core race but theoretically should scale up easily.

##### Life expectancy

Work has begun on creating the statistical methods for life expectancy (see DeathAgeCalculator). Adapting the Weibull distribution a distribution is implemented that calculates the scalar_survival rate (e.g. 100 people born, X many alive at 50 yo). 

This has been adapted to provide probability of death at each year - allowing future modifiers to be applied to increase death probabilities at any given time without a preset death age.

### Communities

Communities are in very early stages, however the basic structure has been developed. It is envisaged that groups of people will reside in a community, allowing people to migrate between communities.

### Corporations

When the time comes, people will have corporations. At first this will be as simple as
Joe Bloggs owns a mill, employs 2 people, they do millwork. In future I would like to see
it progress into simulating some basic financial investment AI as to when
companies are started, companies failing, etc.

## Unit testing

### People

Unit testing has been set up for testing people. This will need to be exponentially added on to keep up with movement of objects.

## Future steps

Plans have been undertaken to figure out how to model families (e.g. with a seperate object or all internal to the person). Thought has also gone into power dynamics and economics.

Core functionality around simulation will need to be developed soon - e.g. being able to simulate iterations of growth.
