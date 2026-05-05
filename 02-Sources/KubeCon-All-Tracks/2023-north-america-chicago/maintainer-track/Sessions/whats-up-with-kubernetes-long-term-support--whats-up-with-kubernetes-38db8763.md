---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2023 - Chicago, United States"
event_id: kccncna2023
year: 2023
region: "North America"
city: "Chicago"
country: "United States"
event_date: "2023-11-06/2023-11-09"
track: "Maintainer Track"
themes: ["AI ML", "Kubernetes Core", "Community Governance"]
speakers: ["Jeremy Rickard", "Microsoft"]
sched_url: https://kccncna2023.sched.com/event/1R2tj/whats-up-with-kubernetes-long-term-support-jeremy-rickard-microsoft
youtube_search_url: https://www.youtube.com/results?search_query=What%27s+up+with+Kubernetes+Long+Term+Support%3F+CNCF+KubeCon+2023
slides: []
status: parsed
---

# What's up with Kubernetes Long Term Support? - Jeremy Rickard, Microsoft

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2023 - Chicago, United States
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Kubernetes Core]], [[Community Governance]]
- País/cidade: United States / Chicago
- Speakers: Jeremy Rickard, Microsoft
- Schedule: https://kccncna2023.sched.com/event/1R2tj/whats-up-with-kubernetes-long-term-support-jeremy-rickard-microsoft
- Busca YouTube: https://www.youtube.com/results?search_query=What%27s+up+with+Kubernetes+Long+Term+Support%3F+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre What's up with Kubernetes Long Term Support?.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2023.sched.com/event/1R2tj/whats-up-with-kubernetes-long-term-support-jeremy-rickard-microsoft
- YouTube search: https://www.youtube.com/results?search_query=What%27s+up+with+Kubernetes+Long+Term+Support%3F+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=0fngdOlwZtQ
- YouTube title: What's up with Kubernetes Long Term Support? - Jeremy Rickard, Microsoft
- Match score: 0.851
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/whats-up-with-kubernetes-long-term-support/0fngdOlwZtQ.txt
- Transcript chars: 36889
- Keywords: working, support, versions, releases, little, version, release, pretty, probably, upgrades, longer, discussion, interesting, survey, months, question, couple, around

### Resumo baseado na transcript

my name is Jeremy I am a co-chair of sigas and I'm co-chairing the working group LTS I'm also an engineer at Microsoft Azure um today we're going to talk about what's up with kubernetes LTS and in this we're going to talk a little bit of History kind of give give some um some insight into where we've been uh this is not the first time that the topic of long-term support uh which is a a nebulous phrase uh has come up in the community so we'll give

### Excerpt da transcript

my name is Jeremy I am a co-chair of sigas and I'm co-chairing the working group LTS I'm also an engineer at Microsoft Azure um today we're going to talk about what's up with kubernetes LTS and in this we're going to talk a little bit of History kind of give give some um some insight into where we've been uh this is not the first time that the topic of long-term support uh which is a a nebulous phrase uh has come up in the community so we'll give a little bit of background there and then we'll talk about what we've started to do with the current iteration of the working group and how folks can uh be involved and help us out with that but first let's talk about why this topic is perhaps um interesting to folks so we've got a a a survey here and it's looking at which hosts are running which kubernetes versions um that are more than 18 months old the tech is a little bit small but you can see that there's a large portion of these things um that seem to be running older versions and and the tail kind of clumps around certain versions it looks like uh we don't have a really big thing at the very end but there there's definitely a peak in there same survey and this was these both were both um from a data dog survey uh showed that over 30% of hosts were running a container D version that was unsupported at the time so we've got kubernetes and container D seems like uh both of these these Technologies are are maybe things that are a little difficult for folks to to deal with and and I think the question that's driving the working group now and I think maybe in the past was why why is that what is the underlying cause for that so this is a quote from previous working group notes uh minor updates which would be going from 1.x so we'll set some some terminology there kubernetes minor versions are going to be 1.20 so 1.21 something like that kubernetes patch versions are going to be something like 120.0 to 120.1 um so the the quote from this end user was that minor upgrades so going from 1.20 to 1.21 for instance feel like major upgrade updates and they're happening too fast and too quickly for people to to quite keep up with so couple things to unpack from that uh they happening too fast uh we'll get to that in a little bit but also they feel like major updates so so what's what's the what's the reason for that well if you've ever worked in software I think uh there's always a push and pull between velocity and features and supportability and fixing things so there's
