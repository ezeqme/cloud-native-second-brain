---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands"
event_id: kccnceu2023
year: 2023
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2023-04-17/2023-04-21"
track: "Maintainer Track"
themes: ["AI ML", "SRE Reliability", "Community Governance"]
speakers: ["Arthur Schreiber", "Github", "Florent Poinsard", "PlanetScale"]
sched_url: https://kccnceu2023.sched.com/event/1Hzda/introduction-to-vitess-and-real-world-usage-arthur-schreiber-github-florent-poinsard-planetscale
youtube_search_url: https://www.youtube.com/results?search_query=Introduction+to+Vitess+and+Real+World+Usage+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Introduction to Vitess and Real World Usage - Arthur Schreiber, Github & Florent Poinsard, PlanetScale

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[SRE Reliability]], [[Community Governance]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Arthur Schreiber, Github, Florent Poinsard, PlanetScale
- Schedule: https://kccnceu2023.sched.com/event/1Hzda/introduction-to-vitess-and-real-world-usage-arthur-schreiber-github-florent-poinsard-planetscale
- Busca YouTube: https://www.youtube.com/results?search_query=Introduction+to+Vitess+and+Real+World+Usage+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Introduction to Vitess and Real World Usage.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2023.sched.com/event/1Hzda/introduction-to-vitess-and-real-world-usage-arthur-schreiber-github-florent-poinsard-planetscale
- YouTube search: https://www.youtube.com/results?search_query=Introduction+to+Vitess+and+Real+World+Usage+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=C2DsT1_zK_4
- YouTube title: Introduction to Vitess and Real World Usage - Arthur Schreiber, Github & Florent Poinsard
- Match score: 0.757
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/introduction-to-vitess-and-real-world-usage/C2DsT1_zK_4.txt
- Transcript chars: 34243
- Keywords: cluster, replicas, basically, support, features, actually, github, around, queries, changes, primary, schema, across, vitess, question, clusters, second, running

### Resumo baseado na transcript

hello everyone um we're here to give you an introduction of the test and present to you a real world usage of vitess so I'm here with Arthur who's a software engineer at GitHub and also a maintainer of the Vitas project and my name is Florent I'm a software engineer at Planet skill the company behind vitess and I'm also a maintainer of vitess So today we're going to give you a brief overview of what is vitess try to explain how does it work why we have the if they wanted to changes um on this cluster okay um so our current architecture for the test is basically built on top of our MySQL setup as I mentioned before um we don't have like we don't do what I would call like a best practice we test it up where everything runs in kubernetes and like like automatically scaled and we have tiny shards and all that stuff um we run BT tablets alongside MySQL on bare metal hosts um the only thing that we run in kubernetes

### Excerpt da transcript

hello everyone um we're here to give you an introduction of the test and present to you a real world usage of vitess so I'm here with Arthur who's a software engineer at GitHub and also a maintainer of the Vitas project and my name is Florent I'm a software engineer at Planet skill the company behind vitess and I'm also a maintainer of vitess So today we're going to give you a brief overview of what is vitess try to explain how does it work why we have the test in the first place and then Arthur will move on to vitessa GitHub so what they had before vitess why did they decide to move to the test and how does it look now that they have fittest instead of the old solution then we'll move on to new and upcoming features and we'll finish with some question answers and resources for you to learn more about your tests uh so before I get started I just want to do like a quick survey who knows like who have heard about vitess before in the sense like did you play with the test did you touch the test in the past just raise your hand okay cool that's a lot more than I expected I'm happy all right what is v test so v test is a scalable distributed Cloud native database system built around MySQL the main goal of your test is to be a seamless replacement for your mystical and it was it is part sorry of the cncf it is a graduated project I think it reached graduation around 2019 and it originally started as a skating solution for my SQL at YouTube around 2010.

so it was created at YouTube it grew in YouTube and in 2018 YouTube donated the whole project to this to the cncf is massively scalable this is uh thanks to sharding and it is also highly available so we run MySQL in replicated mode so we have primaries we have replicas which means that whenever you have a node that like a primary node that fails we can fade over to the replica which is why it is highly available vtest is compatible with mySQL 5.7 mysql80 it used to be also compatible with Maria DB but since the two code bases uh diverged myodb in MySQL we prefer to focus only on my SQL uh Vitesse is used by many large deployments small or large deployments uh over the world um it's not all the names I know that Activision is also using B test uh just a quick survey who is using vitess in production here okay cool yeah GitHub and Activision uh cool all right among all of this we have some key adopters uh slack who's a hundred percent on the test they wrote a very good blog post which is linked right at the bottom
