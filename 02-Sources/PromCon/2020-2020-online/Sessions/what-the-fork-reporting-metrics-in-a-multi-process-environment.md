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
source_url: https://promcon.io/2020-online/talks/what-the-fork-reporting-metrics-in-a-multi-process-environment/
youtube_url: https://www.youtube.com/watch?v=Or_LMxyHwWY
youtube_search_url: https://www.youtube.com/results?search_query=What+the+fork%E2%80%BD+Reporting+metrics+in+a+multi-process+environment+PromCon+2020
video_match_score: 1.016
status: video-found
---

# What the fork‽ Reporting metrics in a multi-process environment

## Identificação

- Edição: PromCon Online 2020
- País/cidade: Online / Online
- Temas: [[Prometheus Core]], [[Metrics]], [[Scalability Reliability]]
- Speakers: N/A
- Página oficial: https://promcon.io/2020-online/talks/what-the-fork-reporting-metrics-in-a-multi-process-environment/
- YouTube: https://www.youtube.com/watch?v=Or_LMxyHwWY

## Resumo

Speaker: Daniel Magliola For many years, most Ruby applications couldn't use Prometheus, because the Ruby client didn't support pre-fork servers. It turns out this wasn't solved for such a long time because it's a surprisingly hard problem. Many have tried to solve this with different approaches, but we found the best one to be the simplest.

## Abstract oficial

Speaker: Daniel Magliola

For many years, most Ruby applications couldn't use Prometheus, because the Ruby client didn't support pre-fork servers.

It turns out this wasn't solved for such a long time because it's a surprisingly hard problem.

Many have tried to solve this with different approaches, but we found the best one to be the simplest.

Let me show you the dark arts of inter-process communication, and how we ended up fully supporting metrics in Ruby.

## Links

- Página oficial: https://promcon.io/2020-online/talks/what-the-fork-reporting-metrics-in-a-multi-process-environment/
- YouTube: https://www.youtube.com/watch?v=Or_LMxyHwWY
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=Or_LMxyHwWY
- YouTube title: PromCon EU 2019: What the Fork‽ Reporting Metrics in a Multi-process Environment
- Match score: 1.016
- Transcript file: _sources/transcripts/youtube-enriched/promcon/2020/what-the-fork-reporting-metrics-in-a-multi-process-environment/Or_LMxyHwWY.txt
- Transcript chars: 30699
- Keywords: pretty, memory, processes, actually, process, client, running, metrics, basically, prometheus, separate, trying, numbers, little, microsecond, labels, performance, stores

### Resumo baseado na transcript

[Music] so this is gonna be a slightly different talk to the previous ones we're gonna be looking at exporting metrics from the application side now last year we decided to revamp the Prometheus ruby client to bring it up to the standards of the other clients and I'm gonna talk a bit more about what that means and it was an interesting project I hope you'll find this this interesting first of all though hi my name is Daniel and I work at go Carles we are a payments

### Excerpt da transcript

[Music] so this is gonna be a slightly different talk to the previous ones we're gonna be looking at exporting metrics from the application side now last year we decided to revamp the Prometheus ruby client to bring it up to the standards of the other clients and I'm gonna talk a bit more about what that means and it was an interesting project I hope you'll find this this interesting first of all though hi my name is Daniel and I work at go Carles we are a payments company based in London now as you probably noticed I'm not originally from London I come from Argentina so if you were wondering that's the accent now for us ago catalyst uptime is critical and that means among other things that having good metrics for our apps is critical and as you probably guessed by the conference name we use Prometheus for this now we're not Prometheus but we had a pretty big issue trying to use it from groovy which is what our main app is written in know as you know promises will periodically scrape your app asking for metrics so we have wraps which in our case again mainly written in Ruby and I'll keeping a bunch of counters in there Prometheus hits you every few seconds and you respond with something that looks a little bit like this and for most languages you just use the appropriate client library and the story ends there however in Ruby lengths and also by the way in Python lengths the story is a little bit trickier because Ruby and Python have a global interpreter lock or Gil which basically doesn't let your app code running multiple threads at the same time so our web servers tend to not be multi-threaded that doesn't parallelize very well instead we tend to use separate processes right processes don't share memory which ends up solving the same problem that Gil was trying to solve and everybody can happily run in parallel ignoring each other this is for example how unicron works which is one of the most common web servers in Ruby so when you recon starts it will load your app and it will fork itself into a master orchestrated process and a bunch of worker processes that are actually going to work on them when a request comes in promises will pick a worker that is free and will send it at a question and take the response and send it back to the client now this system works great it scales really well across course and is how I would say the majority of Ruby web applications and running in production however for the primitives use case this is a bit of a problem we
