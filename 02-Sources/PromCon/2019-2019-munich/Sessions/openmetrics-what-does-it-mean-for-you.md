---
type: promcon-talk
conference: PromCon
edition: "PromCon EU 2019"
edition_id: 2019-munich
year: 2019
city: "Munich"
country: "Germany"
topics: ["Prometheus Core", "Metrics", "Scalability Reliability"]
speakers: []
source_url: https://promcon.io/2019-munich/talks/openmetrics-what-does-it-mean-for-you/
youtube_url: https://www.youtube.com/watch?v=orV4hrk0fJM
youtube_search_url: https://www.youtube.com/results?search_query=OpenMetrics%3A+What+Does+It+Mean+for+You+PromCon+2019
video_match_score: 0.952
status: video-found
---

# OpenMetrics: What Does It Mean for You

## Identificação

- Edição: PromCon EU 2019
- País/cidade: Germany / Munich
- Temas: [[Prometheus Core]], [[Metrics]], [[Scalability Reliability]]
- Speakers: N/A
- Página oficial: https://promcon.io/2019-munich/talks/openmetrics-what-does-it-mean-for-you/
- YouTube: https://www.youtube.com/watch?v=orV4hrk0fJM

## Resumo

Speaker: Brian Brazil The OpenMetrics format intends to standardise metric exposition, making it easy for both those developing and operating systems to monitor them. It is however a new format. Will it be supported by your monitoring system?

## Abstract oficial

Speaker: Brian Brazil

The OpenMetrics format intends to standardise metric exposition, making it easy for both those developing and operating systems to monitor them. It is however a new format. Will it be supported by your monitoring system? Will you need to rewrite your existing instrumentation? What's needed to transition? What about 3rd party systems you don't control? How does this differ and expand, and improve on the existing Prometheus format? This session will cover all of these questions.



Video link -
Slides

## Links

- Página oficial: https://promcon.io/2019-munich/talks/openmetrics-what-does-it-mean-for-you/
- YouTube: https://www.youtube.com/watch?v=orV4hrk0fJM
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=orV4hrk0fJM
- YouTube title: PromCon EU 2019: OpenMetrics: What Does It Mean for You
- Match score: 0.952
- Transcript file: _sources/transcripts/youtube-enriched/promcon/2019/openmetrics-what-does-it-mean-for-you/orV4hrk0fJM.txt
- Transcript chars: 28901
- Keywords: metrics, client, format, actually, standard, prometheus, rather, python, metric, support, seconds, libraries, looking, talking, monitoring, pretty, exemplars, everything

### Resumo baseado na transcript

[Music] hello so starting in front of you again this time actually speaking and we're going to look at open metrics which some of you have simply heard about we're looking to MIT for more I presume you largely know who I am among the list is that I'm one of the people for the last three years now how I have been talking like once every two weeks about open metrics to try and solidify this down so last year Richie was standing up here talking about open metrics

### Excerpt da transcript

[Music] hello so starting in front of you again this time actually speaking and we're going to look at open metrics which some of you have simply heard about we're looking to MIT for more I presume you largely know who I am among the list is that I'm one of the people for the last three years now how I have been talking like once every two weeks about open metrics to try and solidify this down so last year Richie was standing up here talking about open metrics okay this is no happy will remember this moment so last year as I said Richard was up here talking about open metrics it was lot of the theory about why we're doing it but not what it actually is in the actual details which we have now almost completely worked out so what I want to take you through is how it actually matters to you what difference is going to make to you as per meatiest users and as part of the monitoring ecosystem more broadly so a recap which some of Richie covered in his modbus talk that the closest thing we've heard to a metric standard is SNMP and for its age and it's actually pretty good the data model isn't that far off prettiest like it has labels for call tables and it has lots of problems which don't help its scaling so it's very chatty and doesn't have windowing which basically means it's slow the fact that it is polar pushed or whatnot is irrelevant the fact it's very chatty without windowing and there's lots of cases where vendors might be following like the letter of the law like yes that is syntactically a valid SNMP message but why are you putting a float in a string rather than using the float standard which net was never standardized unfortunately einar's order weird stuff let's put multiple floats in there separated by commas cuz that's definitely going to be easy to parse so in many cases you end up having to parse English which is always fun because well I can't get a computer to parse English I need tell us what to do I'm and there's also various utter as various formats like staff see actually that formats pretty popular Graphite's popular and in books to be was there for a while if you want to achieve just one of them but otherwise like there isn't aren't really standard protocols that you're going to come across yeah I just didn't like those two words and so that's kind of a bit of a problem but the good news is - prettiest and particular it's text format became a de facto standard somewhere around two to three years ago to paying away where you couch it's ob
