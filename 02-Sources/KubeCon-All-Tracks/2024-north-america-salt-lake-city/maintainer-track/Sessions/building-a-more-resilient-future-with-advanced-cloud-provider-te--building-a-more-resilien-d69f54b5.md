---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States"
event_id: kccncna2024
year: 2024
region: "North America"
city: "Salt Lake City"
country: "United States"
event_date: "2024-11-12/2024-11-15"
track: "Maintainer Track"
themes: ["AI ML", "SRE Reliability", "Community Governance"]
speakers: ["Michael McCune", "Red Hat", "Bridget Kromhout", "Microsoft"]
sched_url: https://kccncna2024.sched.com/event/1hoyJ/building-a-more-resilient-future-with-advanced-cloud-provider-testing-michael-mccune-red-hat-bridget-kromhout-microsoft
youtube_search_url: https://www.youtube.com/results?search_query=Building+a+More+Resilient+Future+with+Advanced+Cloud+Provider+Testing+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Building a More Resilient Future with Advanced Cloud Provider Testing - Michael McCune, Red Hat & Bridget Kromhout, Microsoft

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[SRE Reliability]], [[Community Governance]]
- País/cidade: United States / Salt Lake City
- Speakers: Michael McCune, Red Hat, Bridget Kromhout, Microsoft
- Schedule: https://kccncna2024.sched.com/event/1hoyJ/building-a-more-resilient-future-with-advanced-cloud-provider-testing-michael-mccune-red-hat-bridget-kromhout-microsoft
- Busca YouTube: https://www.youtube.com/results?search_query=Building+a+More+Resilient+Future+with+Advanced+Cloud+Provider+Testing+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Building a More Resilient Future with Advanced Cloud Provider Testing.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1hoyJ/building-a-more-resilient-future-with-advanced-cloud-provider-testing-michael-mccune-red-hat-bridget-kromhout-microsoft
- YouTube search: https://www.youtube.com/results?search_query=Building+a+More+Resilient+Future+with+Advanced+Cloud+Provider+Testing+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=5FKMFlooC6c
- YouTube title: Building a More Resilient Future with Advanced Cloud Provider Testing - M. McCune, B. Kromhout
- Match score: 0.953
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/building-a-more-resilient-future-with-advanced-cloud-provider-testing/5FKMFlooC6c.txt
- Transcript chars: 33023
- Keywords: provider, testing, absolutely, providers, important, little, controller, looking, controllers, release, infrastructure, talking, specific, actually, interface, probably, interesting, thinking

### Resumo baseado na transcript

all right uh welcome to building a more resilient future with Advanced cloud provider testing uh see I'm Bridget cromhout um I am a product manager at Microsoft Azure and I'm a co-chair of Sig Club provider and uh very active in a number of kubernetes related communities I think that I think ELO and I overlap in at least two or three other communities as well yeah definitely you you definitely get into several communities here uh my name is Michael mun and I'm a software engineer at Red

### Excerpt da transcript

all right uh welcome to building a more resilient future with Advanced cloud provider testing uh see I'm Bridget cromhout um I am a product manager at Microsoft Azure and I'm a co-chair of Sig Club provider and uh very active in a number of kubernetes related communities I think that I think ELO and I overlap in at least two or three other communities as well yeah definitely you you definitely get into several communities here uh my name is Michael mun and I'm a software engineer at Red Hat uh I am the other co-chair of Sig cloud provider uh and I tend to work on cloud provider related things and I also maintain uh cluster autoscaler and the new Carpenter cluster API provider so uh what are we going to talk about today we're going to start by talking a little bit about the history of cloud providers in kubernetes then we're going to talk about testing and why Cloud controllers uh make it complicated and I think this is this is kind of the the high level overview like we will break down a lot more specifics around how we're going to include more providers and testing but probably the the important thing to realize here is that there's a lot going on in cloud provider testing but you don't have to work at a cloud provider to participate in it so we're going to start by looking at a little kubernetes history lesson here uh and we did a little research to look into the history of cloud providers in kubernetes to help set up the context for what we're talking about today so back way way back in about two two 2016 late 2015 when 1.0 uh kubernetes was tagged cloud provider code existed in kubernetes at that time and when I was looking back at this you know we saw the some of the big names that we're familiar with like you know your aws's and your gcps uh but I thought it was interesting there was also a maos uh provider in there as well um I don't know when that got removed but it was just interesting to see um and as we go forward we get up to the 1.13 release and at this point when we look through the history of of git issues we can see the kubernetes community is already starting to interrogate itself about should we have this cloud provider specific code in the core yeah and that's I think that's the important point there is we realize is that there were pros and cons to everything but as the proliferation of cloud providers continued it really didn't make sense to have it um embedded and mingled into the core and we're thinking okay great so then we remove C
