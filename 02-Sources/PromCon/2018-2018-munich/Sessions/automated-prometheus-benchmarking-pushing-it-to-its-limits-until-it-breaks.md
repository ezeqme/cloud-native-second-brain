---
type: promcon-talk
conference: PromCon
edition: "PromCon 2018"
edition_id: 2018-munich
year: 2018
city: "Munich"
country: "Germany"
topics: ["Prometheus Core", "Scalability Reliability"]
speakers: []
source_url: https://promcon.io/2018-munich/talks/automated-prometheus-benchmarking/
youtube_url: https://www.youtube.com/watch?v=9LuVvVddJjg
youtube_search_url: https://www.youtube.com/results?search_query=Automated+Prometheus+Benchmarking+-+Pushing+It+to+Its+Limits+until+It+Breaks%21+PromCon+2018
video_match_score: 0.68
status: video-found
---

# Automated Prometheus Benchmarking - Pushing It to Its Limits until It Breaks!

## Identificação

- Edição: PromCon 2018
- País/cidade: Germany / Munich
- Temas: [[Prometheus Core]], [[Scalability Reliability]]
- Speakers: N/A
- Página oficial: https://promcon.io/2018-munich/talks/automated-prometheus-benchmarking/
- YouTube: https://www.youtube.com/watch?v=9LuVvVddJjg

## Resumo

Speakers: Krasi Georgiev Harsh Agarwal We will show you how we are trying to make Prometheus more stable by running automated benchmarking for risky PRs and before every release. In other words, let's try to break it in our tests so it doesn't break in your production. We will cover why we decided to use Prow and how it is integrated with GitHub.

## Abstract oficial

Speakers:


Krasi Georgiev
Harsh Agarwal


We will show you how we are trying to make Prometheus more stable by running automated benchmarking for risky PRs and before every release. 
In other words, let's try to break it in our tests so it doesn't break in your production.

We will cover why we decided to use Prow and how it is integrated with GitHub.

We will also cover the current progress, the project roadmap and of course do a short demo.



Video link -
Slides

## Links

- Página oficial: https://promcon.io/2018-munich/talks/automated-prometheus-benchmarking/
- YouTube: https://www.youtube.com/watch?v=9LuVvVddJjg
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=9LuVvVddJjg
- YouTube title: PromCon 2018: Automated Prometheus Benchmarking
- Match score: 0.68
- Transcript file: _sources/transcripts/youtube-enriched/promcon/2018/automated-prometheus-benchmarking-pushing-it-to-its-limits-until-it-br/9LuVvVddJjg.txt
- Transcript chars: 16748
- Keywords: prometheus, results, benchmarking, another, version, maintainer, single, release, servers, google, github, decided, cluster, create, benchmark, master, server, deployed

### Resumo baseado na transcript

okay my name is Chrissy I have seen many people read it is crazy and I don't mind it fits very well with the things I like to do in my weekends so that's fine prometheus maintainer from March this year and since then I managed to fix and break quite a few things already work is part of the Prometheus teaming red hot which means mainly fixing bugs and adding features upstream in red hot prometheus is used in OpenShift of course Jiali which is the new open-source project

### Excerpt da transcript

okay my name is Chrissy I have seen many people read it is crazy and I don't mind it fits very well with the things I like to do in my weekends so that's fine prometheus maintainer from March this year and since then I managed to fix and break quite a few things already work is part of the Prometheus teaming red hot which means mainly fixing bugs and adding features upstream in red hot prometheus is used in OpenShift of course Jiali which is the new open-source project for monitoring in tracing of containers and as far as I know in the operations monitoring harsh who is here with me today he is an undergraduate student from the Indian Institute of Technology of Hyderabad who decided to help us through the google Summer of Code so it's great - it's great to having him here so now back to the main part everybody wants stable soft right but how do we know it's stable well in prometheus case that means earning it long enough and high load comparing comparing it with another version and then the results should give us the answer if it's ready for another release or it needs more work to be done well the project is not 100% there yet but we're very very close and the funny story is that when I submitted the talk this was just an idea and maybe some discussions but when I received the email one day saying your talk is accepted that I thought oh no now I really have to do it so lucky for me harsh also liked the idea and decided to help us so I thought well - is a team so there's there is no excuse we can do it no problem so let me see some hands how many of you are some sort of like maintainer Zoar open-source project maintainer okay so you will like the the I promise you will like the next few slides this is what a normal day looks like for me that's just before I look at the github homepage hoping to see a PAPR that is only a single line and the fix is at least two or three bucks but this is what I get next now this might sound and look familiar to many of you usually it starts my prometheus is broken please help so here I keep it calm trying to ask for more details Amen I'm not a psychic give me some detail and this is what I get next it's like a huge config which is supposed to work on like amazing three hundred and thirty five hundred targets now don't get me wrong this is amazing I mean Prometheus can handle that but how do i replicate this locally right well benchmarking and ok let me see some hands how many of you use to point one or two points to version
