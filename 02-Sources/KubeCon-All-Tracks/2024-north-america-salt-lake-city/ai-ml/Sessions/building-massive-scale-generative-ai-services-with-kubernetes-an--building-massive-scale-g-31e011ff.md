---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States"
event_id: kccncna2024
year: 2024
region: "North America"
city: "Salt Lake City"
country: "United States"
event_date: "2024-11-12/2024-11-15"
track: "AI + ML"
themes: ["AI ML", "Kubernetes Core", "SRE Reliability", "Community Governance"]
speakers: ["John McBride", "OpenSauced"]
sched_url: https://kccncna2024.sched.com/event/1i7qI/building-massive-scale-generative-ai-services-with-kubernetes-and-open-source-john-mcbride-opensauced
youtube_search_url: https://www.youtube.com/results?search_query=Building+Massive-Scale+Generative+AI+Services+with+Kubernetes+and+Open+Source+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Building Massive-Scale Generative AI Services with Kubernetes and Open Source - John McBride, OpenSauced

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[AI + ML]]
- Temas: [[AI ML]], [[Kubernetes Core]], [[SRE Reliability]], [[Community Governance]]
- País/cidade: United States / Salt Lake City
- Speakers: John McBride, OpenSauced
- Schedule: https://kccncna2024.sched.com/event/1i7qI/building-massive-scale-generative-ai-services-with-kubernetes-and-open-source-john-mcbride-opensauced
- Busca YouTube: https://www.youtube.com/results?search_query=Building+Massive-Scale+Generative+AI+Services+with+Kubernetes+and+Open+Source+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Building Massive-Scale Generative AI Services with Kubernetes and Open Source.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1i7qI/building-massive-scale-generative-ai-services-with-kubernetes-and-open-source-john-mcbride-opensauced
- YouTube search: https://www.youtube.com/results?search_query=Building+Massive-Scale+Generative+AI+Services+with+Kubernetes+and+Open+Source+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=wYzsPNfMF7A
- YouTube title: Building Massive-Scale Generative AI Services with Kubernetes and Open Source - John McBride
- Match score: 1.002
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/building-massive-scale-generative-ai-services-with-kubernetes-and-open/wYzsPNfMF7A.txt
- Transcript chars: 35390
- Keywords: actually, vector, content, github, search, inside, question, models, inference, cluster, around, better, function, platform, ultimately, series, calling, prompt

### Resumo baseado na transcript

we're going to get started here so this is building massive scale Jer AI services with kubernetes and open source my name is John McBride um I was the head of infrastructure and the lead AI developer at Open sauce which was a small company recently acquired by the Linux Foundation um and I want to do a quick poll um who has built rag applications before or any kind of rag thing okay um who's built like a big kubernetes like tons of gpus a big platform for developers what it looks like today um and some lessons and learnings from this whole product offering so again on the very front end is this thing that we would call the the GitHub events fire hose and really it's just this like constant stream of and pushing those up to azure's container registry um and then Graff alerting on call and basic validation with some of their semantic alerts so nothing fancy like again this time last year I think the sort of how do we do ml Ops was still an open question um so I think there's some great offerings from some companies now um that make deeper validation of your services uh much better so definitely check them out um a quick demo so what I want to show here is actually uh you know this is the part of the demo we all get to look at yaml and stuff but I'm actually show kind of how this would work from inside of the cluster as well um so first going into the Nvidia device plug-in

### Excerpt da transcript

we're going to get started here so this is building massive scale Jer AI services with kubernetes and open source my name is John McBride um I was the head of infrastructure and the lead AI developer at Open sauce which was a small company recently acquired by the Linux Foundation um and I want to do a quick poll um who has built rag applications before or any kind of rag thing okay um who's built like a big kubernetes like tons of gpus a big platform for developers okay a couple people great um it's funny coming to this talk cuz or I guess coming to this cubec Con cuz in Chicago last year this is the talk I wish I had uh I built a bunch of this stuff and designed a bunch of this stuff and our our rag applications inside of open sace um and it was really like bad like this is not going to be the kind of stuff that you would want to inevitably ship to your Enterprises this was like startup mode we're shipping AI we're trying to find market fit uh we're going to do what we can to save money um and hit some kind of scale that will be impressive to the market um our potential investors so on and so forth so um the thing that we ended up building at open sa is something called Star Search and what it really is is kind of you we called it a co-pilot for your git history but really the idea was to derive unique insights and understandings off of get uh GitHub PLL requests and issues and try to go a little deeper than something like GitHub co-pilot um this thing you could you know get in the chat interface we've all seen these kind of chat interfaces before you could ask a unique question so this question here in this example I asked you know who are the best developers that know tailwind and are also interested in Rust and then through poll requests issues a bunch of the metrics and data that we consumed we could then give some interesting answers um when I first built and stubbed this thing out like many of us I used a a service just an inference service like anthropic or open Ai and our initial bill was Absolut absolutely astronomic you can't really see it on the slide here but um this was just like 4 days and it was already like $4,000 plus Dollar in spend um I did some quick back of the napkin math and looking at it it was going to be you know something like let me see I got to actually read these um using gp4 it was going to be like $30 per 1 million tokens input and $60 per 1 million output tokens and again remember this is all like last year when I designe
