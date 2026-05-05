---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2024 - Paris, France"
event_id: kccnceu2024
year: 2024
region: "Europe"
city: "Paris"
country: "France"
event_date: "2024-03-19/2024-03-22"
track: "Maintainer Track"
themes: ["AI ML", "Community Governance"]
speakers: ["Saswata Mukherjee", "Daniel Mohr", "Red Hat"]
sched_url: https://kccnceu2024.sched.com/event/1Yhi5/thanos-infinity-stones-and-how-you-can-operate-them-saswata-mukherjee-daniel-mohr-red-hat
youtube_search_url: https://www.youtube.com/results?search_query=Thanos%E2%80%99+Infinity+Stones+and+How+You+Can+Operate+Them%21+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Thanos’ Infinity Stones and How You Can Operate Them! - Saswata Mukherjee & Daniel Mohr, Red Hat

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Community Governance]]
- País/cidade: France / Paris
- Speakers: Saswata Mukherjee, Daniel Mohr, Red Hat
- Schedule: https://kccnceu2024.sched.com/event/1Yhi5/thanos-infinity-stones-and-how-you-can-operate-them-saswata-mukherjee-daniel-mohr-red-hat
- Busca YouTube: https://www.youtube.com/results?search_query=Thanos%E2%80%99+Infinity+Stones+and+How+You+Can+Operate+Them%21+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Thanos’ Infinity Stones and How You Can Operate Them!.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1Yhi5/thanos-infinity-stones-and-how-you-can-operate-them-saswata-mukherjee-daniel-mohr-red-hat
- YouTube search: https://www.youtube.com/results?search_query=Thanos%E2%80%99+Infinity+Stones+and+How+You+Can+Operate+Them%21+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=e8kvX6mRlyE
- YouTube title: Thanos’ Infinity Stones and How You Can Operate Them! - Saswata Mukherjee & Daniel Mohr, Red Hat
- Match score: 0.809
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/thanos-infinity-stones-and-how-you-can-operate-them/e8kvX6mRlyE.txt
- Transcript chars: 28776
- Keywords: thanos, metrics, actually, clusters, prometheus, operator, cluster, components, infinity, monitoring, remote, customers, certain, receive, storage, global, across, analytics

### Resumo baseado na transcript

so hi everyone so glad to see you all here especially on like the last day of cubec con um hope your conference went well and you were able to learn some cool stuff visit some cool boots maybe grab some stickers as well um so this talk will be a little bit like a case study with some examples and these examples will kind of give you an idea of certain unique things that you can do with Thanos to derive more value from it so a quick show of to global scale and this is where Thanos kind of steps in so if you haven't already heard of Thanos it is a distributed and scalable monitoring system system based on Prometheus with highly available and scalable components that provide you with a global view of all your metrics and long-term storage and querying with features like down sampling and even multi-tenancy it can actually be termed as a sort of distributed Prometheus Plus+ as it distributes parts of Prometheus like the rule engine query engine scrape engine and

### Excerpt da transcript

so hi everyone so glad to see you all here especially on like the last day of cubec con um hope your conference went well and you were able to learn some cool stuff visit some cool boots maybe grab some stickers as well um so this talk will be a little bit like a case study with some examples and these examples will kind of give you an idea of certain unique things that you can do with Thanos to derive more value from it so a quick show of hands um but who knows what an infinity stone is okay so that's a good chunk of you but for those who are uninitiated it's basically a stone that grants you power over some aspect of life and that is what Thanos uses in like the Marvel movies to wipe off the world but we are going to use the Infinity Stones a bit more productively uh here so um an infinity Key Stone for the purposes of this talk is an Innovative way to use Thanos or the data within Thanos uh that kind of enables you to do more with it but before that if you're observant you might have noticed that there's only one speaker on the stage instead of two um sadly my co-speaker Daniel Moore who is a manager for several observability teams at shat had to fly back since his child fell ill but shout out to him for uh his help on the talk and in any case you'll be hearing me yep for like half an hour um so uh time for a quick intro my name is Shasha mukarji I'm a software engineer at Red Hat where I mostly work on monitoring platforms largely based around Thanos I'm also maintainer of Thanos um and was previously a Google summer of code Mente under the same project about 3 years ago and I helped maintain certain other cncf adjacent gotools and libraries and you can find me as um atate s I'm good pretty much uh anywhere so let's start from the basics of all this which at its score is metrics and why we need them to monitor our applications and why do we even need to monitor our applications so whether you fancy on Prem the cloud any hybrid in between you want to make sure that whatever offering you have is actually working most of the time and if it isn't working you want it to call you up at 3:00 a.m.

so that you can fix it so you use tools like preus and alert manager to check on your infrastructure maybe every 30 seconds or so um record that data and alert you when things don't look too good the data model of recording samples or flow values with time stamps and appending it to a Time series is what we commonly call as metrics and simply put it is an aggregatio
