---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Project Opportunities"
themes: ["AI ML", "Storage Data", "Community Governance"]
speakers: ["Matt Lord", "Maintainer"]
sched_url: https://kccnceu2026.sched.com/event/2EFyo/project-lightning-talk-run-your-data-layer-in-k8s-with-vitess-matt-lord-maintainer
youtube_search_url: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Run+Your+Data+Layer+In+K8s+With+Vitess+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Project Lightning Talk: Run Your Data Layer In K8s With Vitess - Matt Lord, Maintainer

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Project Opportunities]]
- Temas: [[AI ML]], [[Storage Data]], [[Community Governance]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Matt Lord, Maintainer
- Schedule: https://kccnceu2026.sched.com/event/2EFyo/project-lightning-talk-run-your-data-layer-in-k8s-with-vitess-matt-lord-maintainer
- Busca YouTube: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Run+Your+Data+Layer+In+K8s+With+Vitess+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Project Lightning Talk: Run Your Data Layer In K8s With Vitess.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2EFyo/project-lightning-talk-run-your-data-layer-in-k8s-with-vitess-matt-lord-maintainer
- YouTube search: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Run+Your+Data+Layer+In+K8s+With+Vitess+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=podkclpdT9E
- YouTube title: Project Lightning Talk: Run Your Data Layer In K8s With Vitess - Matt Lord, Maintainer
- Match score: 0.933
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/project-lightning-talk-run-your-data-layer-in-k8s-with-vitess/podkclpdT9E.txt
- Transcript chars: 5300
- Keywords: cluster, vitess, running, allows, single, database, instance, features, across, course, operator, follow-up, questions, number, future, scaling, remember, everything

### Resumo baseado na transcript

So I'm going to be talking about uh the tests and if you have any follow-up questions, we also have a booth um where we will be there for the first half of each day. So I would encourage you to come by if you have any follow-up questions. Uh query consolidation is another one that if say if you have a a really hot row and a million people come in, request the same row. Uh new Taylor Swift tweet or whatever the case may be, um it will only have to query the database once and then all of the clients can get that same um result. So the the automated recovery is the single biggest thing that you're going to worry about as you scale your data layer. And that's combined with the operator which will of course manage the infrastructure part of that in Kubernetes as an extension of that basic process.

### Excerpt da transcript

Thanks everybody for coming. So I'm going to be talking about uh the tests and if you have any follow-up questions, we also have a booth um where we will be there for the first half of each day. So I would encourage you to come by if you have any follow-up questions. Real briefly about myself. So I I'm a test maintainer. I happen to work at Planet Scale. Um and that's why I'm here. Just a quick show of hands. Who has in the past or is currently using MySQL as your database? Okay, fair number. So, you're kind of the target audience here. U for the rest of you who haven't. I I want the test to kind of be lodged somewhere in the back of your brain so that in the future when you come across a case where where you're working, you're using MySQL and you're running into some scaling challenges that you remember, hey, Beest is a thing. It's a CNCF project that's allows people to scale MySQL. Maybe we should check that out. Um, how many of you people who are have or are using it are actually running MySQL in Kubernetes?

Okay, not too many. And that and that's why I wanted to give this talk because it was a bit surprising to me that so many shops that are all in on Kubernetes are running everything in Kubernetes except their database. that it's it was quite common and still is today to have an RDS instance that is sitting outside of your cluster rather than running that directly in the cluster. So just the very quickly the the value proposition for MySQL is that it allows you to go or for Vitess is that it allows you to go from a single MySQL instance. So you have this single RDS instance let's say and you can scale that out as needed. So you can end up distributing that data layer across hundreds or even thousands of nodes but for your users internal and/or external for them it still appears as as if it was a single MySQL database instance. So some of the key features uh that it provides of course the compatibility is what gives you that facade to your users so that it looks just like it was a single MySQL server but for you as an operator provides a a whole suite of things that allows you to manage this large data layer.

So you can shard and reshard your data. You can add materializations so that you can gain back some of that data locality that you lose when you start distributing your data. So for example, you can have a fact table which exists on all the shards. Uh cluster management of course is a big one as you get into this more complex setup. Uh so it has
