---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Data Processing + Storage"
themes: ["Storage Data", "Kubernetes Core", "SRE Reliability"]
speakers: ["Sarthak Aggarwal", "Madelyn Olson", "AWS"]
sched_url: https://kccnceu2026.sched.com/event/2CW5d/scaling-valkey-the-right-way-kubernetes-at-xl-scale-sarthak-aggarwal-madelyn-olson-aws
youtube_search_url: https://www.youtube.com/results?search_query=Scaling+Valkey+the+Right+Way%3A+Kubernetes+at+XL+Scale+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Scaling Valkey the Right Way: Kubernetes at XL Scale - Sarthak Aggarwal & Madelyn Olson, AWS

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Data Processing + Storage]]
- Temas: [[Storage Data]], [[Kubernetes Core]], [[SRE Reliability]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Sarthak Aggarwal, Madelyn Olson, AWS
- Schedule: https://kccnceu2026.sched.com/event/2CW5d/scaling-valkey-the-right-way-kubernetes-at-xl-scale-sarthak-aggarwal-madelyn-olson-aws
- Busca YouTube: https://www.youtube.com/results?search_query=Scaling+Valkey+the+Right+Way%3A+Kubernetes+at+XL+Scale+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Scaling Valkey the Right Way: Kubernetes at XL Scale.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2CW5d/scaling-valkey-the-right-way-kubernetes-at-xl-scale-sarthak-aggarwal-madelyn-olson-aws
- YouTube search: https://www.youtube.com/results?search_query=Scaling+Valkey+the+Right+Way%3A+Kubernetes+at+XL+Scale+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=t0qax1qQm14
- YouTube title: Scaling Valkey the Right Way: Kubernetes at XL Scale - Sarthak Aggarwal & Madelyn Olson, AWS
- Match score: 0.825
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/scaling-valkey-the-right-way-kubernetes-at-xl-scale/t0qax1qQm14.txt
- Transcript chars: 30845
- Keywords: basically, cluster, clusters, actually, primary, little, replica, connection, shards, primaries, important, replicas, information, around, talking, valkyrie, within, operator

### Resumo baseado na transcript

Uh I'd like to say that me and Sarthik here uh are foreigners in a strange lands both you know we're Americans over here in Europe as well as uh we come from Amazon which is mostly a VM based world. So we're all we look over here at Kubernetes and we're like wow this technology is amazing. And then they scaled four 5x that they're like that's the worst case and the green line is what happened. um which was you know uh it peaked at almost 50 times what they expected uh but the beauty is they talked a lot about how they were built on top of Kubernetes and cloudnative technologies and they were able to basically scale up the Um and that allows you to scale both write capacity and read capacity and everything scales horizontally. So when you add you know a fourth node it will automatically learn about the other nodes in the cluster.

### Excerpt da transcript

Hello. Hello. Welcome everyone. Uh my name is Maline Olsen. Uh we're going to be talking about Valkyrie today. Uh I'd like to say that me and Sarthik here uh are foreigners in a strange lands both you know we're Americans over here in Europe as well as uh we come from Amazon which is mostly a VM based world. So we're all we look over here at Kubernetes and we're like wow this technology is amazing. I wish we could use more of it. Um but we're hoping that we can take some of our learnings that we've seen sort of helping build extremely large clusters uh for caching from the Amazon elastic world which is the in-memory managed caching service that Amazon provides and help provide some you know hopefully useful guidance for this. Um so as I said my name is Meline. I am a principal engineer at Amazon Elastic. Uh and I'm also one of the open source maintainers of Valky. Uh don't worry if you don't know what that is. uh we'll talk about a little bit more in a second and I'm joined with Sarthik uh who is another engineer at Amazon Elasticash and also a uh contributor to the open source Valky project.

Uh so the theme of our talk today is really about you know scaling large clusters and I want to start with a story first about why uh scaling large clusters is important. Um do people here remember the Pokémon Go craze that happened back in 2016? people outgoing um you know wandering around late at night trying to catch Pokemon. Um and I really like the story because they highlighted the fact that um within Niantic they made some projections about how much usage and capacity they were going to need. Um so they kind of you know did some math and figured out that orange line at the bottom that was their baseline. That's how much capacity they thought they would need. And then they scaled four 5x that they're like that's the worst case and the green line is what happened. um which was you know uh it peaked at almost 50 times what they expected uh but the beauty is they talked a lot about how they were built on top of Kubernetes and cloudnative technologies and they were able to basically scale up the whole way and so the thing I want to highlight is um we're going to talk about 200 node clusters for Valky a lot and uh you shouldn't be running those every day in production they are finicky there's basically no vertical scalability of those clusters um but you might have And so the goal of today is sort of how do you be prepared so that if you do end up in a situation whe
