---
type: promcon-talk
conference: PromCon
edition: "PromCon 2017"
edition_id: 2017-munich
year: 2017
city: "Munich"
country: "Germany"
topics: ["Prometheus Core", "Metrics"]
speakers: []
source_url: https://promcon.io/2017-munich/talks/start-your-engines-white-box-monitoring-for-load-tests/
youtube_url: https://www.youtube.com/watch?v=NQ3DYMs6KWc
youtube_search_url: https://www.youtube.com/results?search_query=Start+Your+Engines%3A+White+Box+Monitoring+for+Your+Load+Tests+PromCon+2017
video_match_score: 0.917
status: video-found
---

# Start Your Engines: White Box Monitoring for Your Load Tests

## Identificação

- Edição: PromCon 2017
- País/cidade: Germany / Munich
- Temas: [[Prometheus Core]], [[Metrics]]
- Speakers: N/A
- Página oficial: https://promcon.io/2017-munich/talks/start-your-engines-white-box-monitoring-for-load-tests/
- YouTube: https://www.youtube.com/watch?v=NQ3DYMs6KWc

## Resumo

Speaker: Alexander Schwartz You think monitoring is only for production? Wrong: Add a metrics endpoint to your application to get insights during your load tests - and use them for free to monitor production! This talk shows how to setup up the load testing tools JMeter and Gatling to push their metrics to Prometheus.

## Abstract oficial

Speaker: Alexander Schwartz

You think monitoring is only for production? Wrong: Add a metrics endpoint to your application to get insights during your load tests - and use them for free to monitor production!

This talk shows how to setup up the load testing tools JMeter and Gatling to push their metrics to Prometheus. It also makes the case to expose metrics as part of core application development instead of treating them as a small add-on before go-live.



Video link -
Slides

## Links

- Página oficial: https://promcon.io/2017-munich/talks/start-your-engines-white-box-monitoring-for-load-tests/
- YouTube: https://www.youtube.com/watch?v=NQ3DYMs6KWc
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=NQ3DYMs6KWc
- YouTube title: PromCon 2017: Start Your Engines: White Box Monitoring for Your Load Tests - Alexander Schwartz
- Match score: 0.917
- Transcript file: _sources/transcripts/youtube-enriched/promcon/2017/start-your-engines-white-box-monitoring-for-your-load-tests/NQ3DYMs6KWc.txt
- Transcript chars: 14819
- Keywords: metrics, prometheus, graphite, application, testing, exporter, environment, getting, actually, developers, probably, machine, production, looking, product, usually, monitoring, minutes

### Resumo baseado na transcript

[Music] right so welcome to the talk start your engines white box monitoring for your love tests so the talk yet before was about how to monitor protection and maybe your tools already have metrics that you can expose but now we want to look at how you actually get to your metrics in your product maybe to get your developers to instrument your the application so this is the agenda for the next like 20 minutes why to use load testing in the first place how to set up

### Excerpt da transcript

[Music] right so welcome to the talk start your engines white box monitoring for your love tests so the talk yet before was about how to monitor protection and maybe your tools already have metrics that you can expose but now we want to look at how you actually get to your metrics in your product maybe to get your developers to instrument your the application so this is the agenda for the next like 20 minutes why to use load testing in the first place how to set up an environment with Prometheus for your load tests a short demo that will might probably fall so to to just to be sort of the machine and then what to expect what worked good for us what could have been improved and things to watch out for you could try something like this at work so I'm going to use low test well naive world we have a developer that develops an application on his or her machine and what is then being tested by another human on his or her machine and once you're in production you have lots of users and what Daniel II happens something that you said the catches fire because all the loads of the users and you find out well what could have we done different maybe we could have used some metrics in here but obviously in the first place you didn't put in any metrics and you're lost in production right so let's do it better so let's again have a developer at his or her machine developer software they want to deploy do the testing with some no testing tools with scaling in jmeter and then make your server burn up in flames and well at that point make the developers add some metrics to your software just the metrics they need to find out why it's burning down and as if they have added enough metrics to get the insights they need to pass the low tests only then go into production and well as you have already put in all the white box metrics into the application you can use the same metrics in production that's the basic idea in test environments you might have a short retention time and might also scrape every second in production you might have like 15 days we heard and scrape for every 30 seconds every 60 seconds what fits you best and we tried that approach and let's see what comes out of them so then how to set up an environment for this the technical building blocks that we've seen here well there's the application under test well we are testing Java applications so we put in the driver simple client in our applications and the no testing tool either getting or jmeter both of these
