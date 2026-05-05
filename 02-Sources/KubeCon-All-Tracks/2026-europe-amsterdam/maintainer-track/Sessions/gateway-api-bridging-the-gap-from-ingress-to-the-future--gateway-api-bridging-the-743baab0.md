---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Maintainer Track"
themes: ["AI ML", "Networking", "Community Governance"]
speakers: ["Nick Young", "James Strong", "Isovalent at Cisco", "Katarzyna Łach", "Rostislav Bobrovsky", "Google", "Norwin Schnyder", "Airlock"]
sched_url: https://kccnceu2026.sched.com/event/2EsAI/gateway-api-bridging-the-gap-from-ingress-to-the-future-nick-young-james-strong-isovalent-at-cisco-katarzyna-lach-rostislav-bobrovsky-google-norwin-schnyder-airlock
youtube_search_url: https://www.youtube.com/results?search_query=Gateway+API%3A+Bridging+the+Gap+from+Ingress+to+the+Future+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Gateway API: Bridging the Gap from Ingress to the Future - Nick Young & James Strong, Isovalent at Cisco; Katarzyna Łach & Rostislav Bobrovsky, Google; Norwin Schnyder, Airlock

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Networking]], [[Community Governance]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Nick Young, James Strong, Isovalent at Cisco, Katarzyna Łach, Rostislav Bobrovsky, Google, Norwin Schnyder, Airlock
- Schedule: https://kccnceu2026.sched.com/event/2EsAI/gateway-api-bridging-the-gap-from-ingress-to-the-future-nick-young-james-strong-isovalent-at-cisco-katarzyna-lach-rostislav-bobrovsky-google-norwin-schnyder-airlock
- Busca YouTube: https://www.youtube.com/results?search_query=Gateway+API%3A+Bridging+the+Gap+from+Ingress+to+the+Future+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Gateway API: Bridging the Gap from Ingress to the Future.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2EsAI/gateway-api-bridging-the-gap-from-ingress-to-the-future-nick-young-james-strong-isovalent-at-cisco-katarzyna-lach-rostislav-bobrovsky-google-norwin-schnyder-airlock
- YouTube search: https://www.youtube.com/results?search_query=Gateway+API%3A+Bridging+the+Gap+from+Ingress+to+the+Future+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=_4JkNbuA2Gg
- YouTube title: Gateway API: Bridging the Gap from Ingress to the Future - Panel
- Match score: 1.028
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/gateway-api-bridging-the-gap-from-ingress-to-the-future/_4JkNbuA2Gg.txt
- Transcript chars: 24291
- Keywords: gateway, ingress, connection, client, certificate, features, release, actually, configuration, everyone, applause, listener, please, pretty, thanks, feature, certificates, backend

### Resumo baseado na transcript

I'm a maintainer for ingress engineext for about another hour and I work for uh is valent. [applause] Hi everyone, I'm Rosti, tech lead manager at Google primarily focus on cloud load balancing and also Git API contributor. They will not be fixed by the Kubernetes or um a fork might fix them, but again, they won't be fixed by the main contributors anymore. So, we've already talked about the security piece and we will be archiving the project. If you have any issues with the Helm chart, please let us know in Kubernetes or Kubernetes Slack. Uh we have moved to something a lot more similar to the upstream Kubernetes release and uh so that includes we're sort of moving more as a uh release train.

### Excerpt da transcript

Okay, everyone. We're going to get started because we got a lot to get through today. We have a very packed agenda. Um, those of you still coming in, please come in, find spots. Don't feel bad. There's heaps of spots down the front stage. Stage right, your left. Anyway, uh, okay. So, we're going to get started. Cool. Uh, welcome to bridging the gap from ingress to the future. Uh, we are, uh, talking about gateway API and ingress today. Um, thank you all for coming. This is pretty crazy. Biggest theater I've ever done. most full I've ever seen. Um, so yeah, thank you all for coming again. So, uh, we will get started with round of intros. Um, my name is Nick Young. I'm the leftmost person on the slide. I work for ISO at Cisco and I'm a maintainer on Gateway API. James. >> Hi everyone. My name is James Strong. I'm a maintainer for ingress engineext for about another hour and I work for uh is valent. [applause] Hi everyone, I'm Rosti, tech lead manager at Google primarily focus on cloud load balancing and also Git API contributor.

[clears throat] >> Hello, I'm Katrina. I'm engineer at Google and I'm working with gateway API. >> Hello everyone, I'm Norvin. I'm working at airlock implementing gateway API and also contributing to the project. Cool. Thanks everyone. So today we got a few things to talk about. Uh James is going to run us through the what's going on with uh ingress engineext's uh deprecation and archiving. Um we will talk about I'll talk a little bit about uh what we what gateway API has been doing to make the migration a bit easier. Then we'll go through a bunch of the stuff that we've uh added to the recent uh 1.5 release. Uh and Norman will run us through a funky new uh controller matching wizard that uh that Becca built for us. It's uh pretty sweet. So, uh, but we do only have 30 minutes and we have an awful lot to get through, so we're going to go pretty quick. U, we will try and save some time for Q&A at the end, but if not, uh, we'll be available outside for questions afterwards. So, over to you, James. >> All right, let's go ahead and get this started.

And it doesn't look like it's switching. Oh, okay. Uh, I wanted to do a quick run through just like some of the numbers. Uh, it was really hard actually to find the first commit for this because Ingress EngineX originally wasn't in its own repository. It was in contrib and it was just known as I think like ingress for a while and then they didn't like that name so we changed it. Um but it's
