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
themes: ["AI ML", "Platform Engineering", "Community Governance"]
speakers: ["Filippe Spolti", "Jooho Lee", "Red Hat"]
sched_url: https://kccnceu2026.sched.com/event/2EF54/evolving-kserve-the-unified-model-inference-platform-for-both-predictive-and-generative-ai-filippe-spolti-jooho-lee-red-hat
youtube_search_url: https://www.youtube.com/results?search_query=Evolving+KServe%3A+The+Unified+Model+Inference+Platform+for+Both+Predictive+and+Generative+AI+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Evolving KServe: The Unified Model Inference Platform for Both Predictive and Generative AI - Filippe Spolti & Jooho Lee, Red Hat

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Platform Engineering]], [[Community Governance]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Filippe Spolti, Jooho Lee, Red Hat
- Schedule: https://kccnceu2026.sched.com/event/2EF54/evolving-kserve-the-unified-model-inference-platform-for-both-predictive-and-generative-ai-filippe-spolti-jooho-lee-red-hat
- Busca YouTube: https://www.youtube.com/results?search_query=Evolving+KServe%3A+The+Unified+Model+Inference+Platform+for+Both+Predictive+and+Generative+AI+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Evolving KServe: The Unified Model Inference Platform for Both Predictive and Generative AI.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2EF54/evolving-kserve-the-unified-model-inference-platform-for-both-predictive-and-generative-ai-filippe-spolti-jooho-lee-red-hat
- YouTube search: https://www.youtube.com/results?search_query=Evolving+KServe%3A+The+Unified+Model+Inference+Platform+for+Both+Predictive+and+Generative+AI+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=zcdrXu1Fpy0
- YouTube title: Evolving KServe: The Unified Model Inference Platform for Both Predictive and... F. Spolti & J. Lee
- Match score: 0.964
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/evolving-kserve-the-unified-model-inference-platform-for-both-predicti/zcdrXu1Fpy0.txt
- Transcript chars: 23502
- Keywords: gateway, inference, already, endpoint, request, picker, predictive, everything, deployment, configuration, generative, basically, important, prefill, decode, kserve, nowadays, gpu

### Resumo baseado na transcript

So I really excited to share about the Kerve road map and what is Kerve today. So um in this presentations we kind start work uh talking about say um welcome to Amsterdam right but we are on the last day already. It's more like um having the governance the the production ready uh the security stuff and you know we need to be trustable and what CNF tells to to the world where it's like um okay it was accepted in CNCF it means that CNCF Data scientist essentially does not have too much knowledge about Kubernetes, right? And what it does it kind of um abstract all the all the complexity of configuring network configuring security configuring ingress agress uh etc. So as a users you probably have some of this kind of question how we scale request batching security distribute those are we provided.

### Excerpt da transcript

All right. So, um hello folks. Um I [clears throat] am Phillip. Um I'm a senior software engineer at Red Hat. We work on the inference team. Basically, Ker is our main thing nowadays. Um on the tool we work, right? Want to talk something for >> Hello, my name is Julie. I'm principal uh software engineer at Red Hat. Uh we are same team. We are working on Kserve as a maintainers. So I really excited to share about the Kerve road map and what is Kerve today. Go ahead. So um in this presentations we kind start work uh talking about say um welcome to Amsterdam right but we are on the last day already. So hopefully you guys have some energy left to stay here for one 1 hour and a half. No, >> only 30 minutes. >> Okay. So um just kidding. Uh all right. Okay. So let's get started. All right. So what is what is Kerve based from? Right. So case serve is kind of the main or orchestrator for any model workload any AI workload you might have to to run on coets. So uh in the in the pillar we have the hardware. So basically we can we can have a GPU CPUs and I think TPUs are uh as well is is is kind of supported on Kubernetes.

uh Google has put a lot of effort on that right so why not and in the top layer we have Kubernetes orchestrating everything for us and what Quer really is it's a top layer on top of Kubernetes that handles everything we need to get our models ready running in a production grade uh level right so uh because nowadays what is the most important thing is to have a reliable and possible infrastructure where you can have your workloads running without disruption. Right? So, uh in uh case serve instead of um trying to reinventing stuff to adapt to to our needs, we can adapt the case to use what we have the best already in the market. Right? So the most uh useful tools that we we we have nowadays are already on CNCF are already graduated is our now close friends right I'll get there right right right right right right right right right there so for autoscaling we start with K native but we are now moving to kab and for networking our main guy is the envoy envoy AI gateway uh it has some some cool stuff that you will present later uh and top of this all right uh LLMZ is the main guy that everyone is talking about nowadays, right?

And how why is that so important? Uh is because it makes your inference so fast that you can even compare your largeang language model being serving served locally with the same power than the chat GPT, right? The same the same spe
