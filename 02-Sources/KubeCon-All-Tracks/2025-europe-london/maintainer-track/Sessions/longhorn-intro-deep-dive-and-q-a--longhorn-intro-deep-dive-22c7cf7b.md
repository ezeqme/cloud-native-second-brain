---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom"
event_id: kccnceu2025
year: 2025
region: "Europe"
city: "London"
country: "United Kingdom"
event_date: "2025-04-01/2025-04-04"
track: "Maintainer Track"
themes: ["AI ML", "Community Governance"]
speakers: ["David Ko", "SUSE"]
sched_url: https://kccnceu2025.sched.com/event/1tczj/longhorn-intro-deep-dive-and-qa-david-ko-suse
youtube_search_url: https://www.youtube.com/results?search_query=Longhorn%3A+Intro%2C+Deep+Dive+and+Q%26A+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Longhorn: Intro, Deep Dive and Q&A - David Ko, SUSE

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Community Governance]]
- País/cidade: United Kingdom / London
- Speakers: David Ko, SUSE
- Schedule: https://kccnceu2025.sched.com/event/1tczj/longhorn-intro-deep-dive-and-qa-david-ko-suse
- Busca YouTube: https://www.youtube.com/results?search_query=Longhorn%3A+Intro%2C+Deep+Dive+and+Q%26A+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Longhorn: Intro, Deep Dive and Q&A.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1tczj/longhorn-intro-deep-dive-and-qa-david-ko-suse
- YouTube search: https://www.youtube.com/results?search_query=Longhorn%3A+Intro%2C+Deep+Dive+and+Q%26A+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=REkSMbRrBU4
- YouTube title: Longhorn: Intro, Deep Dive and Q&A - David Ko, SUSE
- Match score: 0.901
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/longhorn-intro-deep-dive-and-q-a/REkSMbRrBU4.txt
- Transcript chars: 24577
- Keywords: replica, performance, volume, support, engine, longhorn, release, backup, actually, storage, better, version, working, capacity, understand, around, together, control

### Resumo baseado na transcript

I attend the qcon's capitalize the main mission for me is promotion longhome to have a more adaptions around the world. So I'm engineering director at susa and leading a long teams working on that together with our external contributors. Longhome is the distributed bar storage solutions uh based on Kubernetes. design and the third one is the not just position volumeings we beyond that we also provide the incluster snup to make So uh you can have a different time and different strategy to manage your local data for your volume. So this is better fit uh if you have any strategy you want to manage your data outside and the foreign storage based on backup is a crossclass disaster disaster recovery because you can leverage centralized backup targets and restore your data to the different domain you are working for to adopt the longhorn for that and of course lon can run on the nodes run your kubernetes uh using the traditional operating system for sure if you look into or read our documentation you will know we each uh

### Excerpt da transcript

Welcome to the session about longhome and I'm David Co. I attend the qcon's capitalize the main mission for me is promotion longhome to have a more adaptions around the world. Okay. So I'm engineering director at susa and leading a long teams working on that together with our external contributors. Okay. So the agenda is about I will talk about longhaul overview and I assume some of you maybe not using use longhaul right now or maybe consider using longhaul and some of you already using nonhong. I will talk about more about plan later. Okay. So after overview we'll be go over the project status updates and the release updates and the next important part is about the longhorn details. So you will know more about how long walk how simply it is and from design from the operation and uh to the day two and whatever you want to manage along in your cluster including the few subtopics architecture and uh capacities we have and most one item I want to individual independent highlight is a v2 data engines.

So this new one we are we are spending lot of effort on that to let the longhorn capacity especi performance jump to the next levels. Okay. And about release and we already released one at in January. So some of you maybe try and one day right now the latest version is 1.1 is the stable versions. So please give it a try or upgrade to it. Give us more feedbacks. and also the upcoming one night in May and there are a couple of new features and new ideal ideas following and we want to do in a foreign release. Okay, this page is a simply let a user note a special for for people you don't know about Longhorn. Longhome is the distributed bar storage solutions uh based on Kubernetes. So you can simply start from a cluster install long chart that's it. So everything layer because you will use your local disk by default and the secondly uh you can provide highly available persist volume because we replica we have a more than one copies of data for your volume but it's configurable depends on your uh design and the third one is the not just position volumeings we beyond that we also provide the incluster snup to make So uh you can have a different time and different strategy to manage your local data for your volume.

So also we provide the external backup. So this is better fit uh if you have any strategy you want to manage your data outside and the foreign storage based on backup is a crossclass disaster disaster recovery because you can leverage centralized backup targ
