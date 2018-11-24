# mochart

[![CircleCI](https://circleci.com/gh/hyunchel/mochart/tree/master.svg?style=svg)](https://circleci.com/gh/hyunchel/mochart/tree/master)

mochart(**m**usic **o**n **chart**) is a simple webpage parser that aims to retrieve song rankings in JSON compatible data format.

## Installation

A simple `pip` install:
```bash
pip install mochart
```

## Example

Realtime ranks from Melon:
```python
from mochart import melon
ranks = melon.realtime()
print(ranks)
```
At the time of this writing, the code would print:
```json
[{
	"title": "SOLO",
	"artist": "제니 (JENNIE)",
	"album": "SOLO"
}, {
	"title": "봄바람",
	"artist": "Wanna One (워너원)",
	"album": "1¹¹=1 (POWER OF DESTINY)"
}, {
	"title": "Tempo",
	"artist": "EXO",
	"album": "DON`T MESS UP MY TEMPO - The 5th Album"
}, {
	"title": "YES or YES",
	"artist": "TWICE (트와이스)",
	"album": "YES or YES"
}, {
	"title": "너를 만나",
	"artist": "폴킴",
	"album": "너를 만나"
}, {
	"title": "아름답고도 아프구나",
	"artist": "비투비",
	"album": "HOUR MOMENT"
}, {
	"title": "Gravity",
	"artist": "EXO",
	"album": "DON`T MESS UP MY TEMPO - The 5th Album"
}...]
```
> feat. 아이돌전쟁

## API

All functions in a provider(e.g. Melon) will return Python List that contains music information in order of its ranking.

Generally, a rank contains title, aritst, and album in string format as seen above.

*Not all providers support the these functions.*

#### realtime
Return the most current ranks at the time of query.

#### trend
Return songs that are trending at the time of query.

#### day
Return ranks given day.

#### week
Return ranks given week.

#### month
Return ranks given month.

#### year
Return ranks given year.


## Datetime

Given datetime object will be converted into a local datetime for the provider. For example A datetime given to `melon.day(today)`, the argument `today` will be converted to  `Asia/Seoul` timezone before the query.

Note that if incorrect time is given to any function, it could return either an empty array or ranks of the closest date.

Also, if no datetime object is provided as an argument, the current time will be used in the query.

## Contribution

You are more than welcome to contribute a new chart and/or ideas on this project.
