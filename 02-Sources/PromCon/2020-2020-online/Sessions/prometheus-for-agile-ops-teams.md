---
type: promcon-talk
conference: PromCon
edition: "PromCon Online 2020"
edition_id: 2020-online
year: 2020
city: "Online"
country: "Online"
topics: ["Prometheus Core", "Metrics", "Scalability Reliability"]
speakers: []
source_url: https://promcon.io/2020-online/talks/prometheus-for-agile-ops-teams/
youtube_url: https://www.youtube.com/watch?v=hioFPMtqc-4
youtube_search_url: https://www.youtube.com/results?search_query=Prometheus+For+Agile+Ops+Teams+PromCon+2020
video_match_score: 0.696
status: video-found
---

# Prometheus For Agile Ops Teams

## Identificação

- Edição: PromCon Online 2020
- País/cidade: Online / Online
- Temas: [[Prometheus Core]], [[Metrics]], [[Scalability Reliability]]
- Speakers: N/A
- Página oficial: https://promcon.io/2020-online/talks/prometheus-for-agile-ops-teams/
- YouTube: https://www.youtube.com/watch?v=hioFPMtqc-4

## Resumo

Speaker: Andrew Burian In this presentation we talk about Axiom Zen’s long and colourful history trying to find a working monitoring solution, and how eventually giving up the silver bullet and working with a vendor neutral solution that we could gradually build out into a complete pipeline was the right way to go. We develop software in an agile fashion, delivering value incrementally, and pivoting as real requirements play out. So too should we build our monitoring.

## Abstract oficial

Speaker: Andrew Burian

In this presentation we talk about Axiom Zen’s long and colourful history trying to find a working monitoring solution, and how eventually giving up the silver bullet and working with a vendor neutral solution that we could gradually build out into a complete pipeline was the right way to go.

We develop software in an agile fashion, delivering value incrementally, and pivoting as real requirements play out. So too should we build our monitoring. There exists no magic bullet for your metrics set up that will work for every team. Only time and hard fought lessons will enable teams to figure out what’s right for your specific case. So why is it that metrics pipeline set up and vendor selection feels like an all or nothing solution? Why do we guess for so long at our requirements, and then laboriously add in vendor specific code just to find in a few weeks, months, years, that you guessed wrong and actually your needs are better served in a different way.
Come learn from some of our most painful lessons.

## Links

- Página oficial: https://promcon.io/2020-online/talks/prometheus-for-agile-ops-teams/
- YouTube: https://www.youtube.com/watch?v=hioFPMtqc-4
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=hioFPMtqc-4
- YouTube title: PromCon Online 2020 - Prometheus For Agile Ops Teams, Andrew Burian @ Dapper Labs
- Match score: 0.696
- Transcript file: _sources/transcripts/youtube-enriched/promcon/2020/prometheus-for-agile-ops-teams/hioFPMtqc-4.txt
- Transcript chars: 28002
- Keywords: prometheus, monitoring, metrics, actually, grafana, assumptions, manager, projects, question, vendor, software, better, around, monitor, change, systems, little, development

### Resumo baseado na transcript

[Music] all right is this thing on can everyone hear me let's get started so this is prometheus for agile teams i'll be your host andrew bierian and in this talk we're talking about delivering value with prometheus enabling us to build monitoring systems the same way we build our software systems in an agile fashion changing requirements uncertain assumptions and continuously delivering value little prerequisite introduction about me i'm andrew um i'm the lead sre at a company called axiom zen and uh i've been involved in the design

### Excerpt da transcript

[Music] all right is this thing on can everyone hear me let's get started so this is prometheus for agile teams i'll be your host andrew bierian and in this talk we're talking about delivering value with prometheus enabling us to build monitoring systems the same way we build our software systems in an agile fashion changing requirements uncertain assumptions and continuously delivering value little prerequisite introduction about me i'm andrew um i'm the lead sre at a company called axiom zen and uh i've been involved in the design and creation of monitoring systems for every one of axiom's ends project for about the last three years we've been running prometheus in production as our standard choice for about three years now and i've helped oversee the launch of very successful projects complete failure projects very small projects and very large projects from kind of all over the spectrum of the software space um if you haven't heard vaccines in before you're not alone but you might notice might know us for one of our other portfolio companies if you use github we made zenhub if you use tabs and chrome we made toby most recently we're famous for crypto kitties we're the company behind dapper labs we made cheese wizards and most most recently nba top shop it's a lot of different projects it's a lot of different spaces and it's been really interesting to build this many different projects in this many different environments but throughout all this you learn that some things are constant in any of these projects regardless of the size or scale and i've found that how you build monitoring is one of them at some point in your monitoring life you will hear a question like this you need to be paying attention to when you when you build your monitoring where you're spending your time and effort because if you hear this question you should raise a flag when you hear this question you might be tempted to roll your eyes so hard you fall out of your chair because the answer is obviously yes do we need to be monitoring yes but if you survive the initial shock of having someone asking this question it's important to look past this and hear what the question actually is because it probably means your team is not getting the value out of your monitoring that they need to be the real question underneath this is what do we need to be monitoring we struggle a lot in all of our projects with the upfront cost of building proper monitoring and do we need to do this right now
