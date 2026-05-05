---
type: kubecon-session
event: "KubeCon + CloudNativeCon China 2025 - Hong Kong, China"
event_id: kccncchn2025
year: 2025
region: "China"
city: "Hong Kong"
country: "China"
event_date: "2025"
track: "Application Development"
themes: ["AI ML"]
speakers: ["Peter Pan", "Neko Ayaka", "Kebe Liu", "DaoCloud"]
sched_url: https://kccncchn2025.sched.com/event/1x5kB/taming-dependency-chaos-for-llm-in-k8s-peter-pan-neko-ayaka-kebe-liu-daocloud
youtube_search_url: https://www.youtube.com/results?search_query=Taming+Dependency+Chaos+for+LLM+in+K8s+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Taming Dependency Chaos for LLM in K8s - Peter Pan, Neko Ayaka & Kebe Liu, DaoCloud

## Identificação

- Edição: KubeCon + CloudNativeCon China 2025 - Hong Kong, China
- Trilha oficial: [[Application Development]]
- Temas: [[AI ML]]
- País/cidade: China / Hong Kong
- Speakers: Peter Pan, Neko Ayaka, Kebe Liu, DaoCloud
- Schedule: https://kccncchn2025.sched.com/event/1x5kB/taming-dependency-chaos-for-llm-in-k8s-peter-pan-neko-ayaka-kebe-liu-daocloud
- Busca YouTube: https://www.youtube.com/results?search_query=Taming+Dependency+Chaos+for+LLM+in+K8s+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Taming Dependency Chaos for LLM in K8s.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncchn2025.sched.com/event/1x5kB/taming-dependency-chaos-for-llm-in-k8s-peter-pan-neko-ayaka-kebe-liu-daocloud
- YouTube search: https://www.youtube.com/results?search_query=Taming+Dependency+Chaos+for+LLM+in+K8s+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=26CaKlujVyI
- YouTube title: Taming Dependency Chaos for LLM in K8s - Peter Pan, Neko Ayaka & Kebe Liu, DaoCloud
- Match score: 0.741
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/taming-dependency-chaos-for-llm-in-k8s/26CaKlujVyI.txt
- Transcript chars: 18408
- Keywords: environment, python, dependency, version, dependencies, docker, another, minutes, everyone, across, production, install, support, machine, create, storage, environments, libraries

### Resumo baseado na transcript

Uh our topic is about to take the dependency chaos for large language model developer in the kubernetes environment. We are engineer from dra and also we are the kubernetes contributor and cave contributors. So the core problem is when Python means C C++ the perfect stone emerge. The real world impact is since any of those problems may occur at any time hours of wasting to install the environments will waste a lot of our time. It's because PIP can see why when we are installing torch or transformers or accelerator it's not we are only install the pietorch itself instead we will need to install GCC make cuda everything relates to cuda and machine learning that's something that pip can Yeah, perhaps we can imagine we can reduce the four to six hours of time cost to less than 30 seconds.

### Excerpt da transcript

Okay, good afternoon everyone. Uh thank you to step up with us. Uh our topic is about to take the dependency chaos for large language model developer in the kubernetes environment. Uh first for to self introduce uh we come from the dock crow. We are engineer from dra and also we are the kubernetes contributor and cave contributors. Uh I'm Peter Pan. Uh and this is Kabio and this is Niko Jang. All right. Uh usually we have facing a lot of challenges uh across AI development uh to the um to the production stage. Uh first uh we have challenge about um the Python and NodeJ developer in dependency installation. not only takes time but also uh the version may shift from different environments and become inconsistency hell and also we have challenge about the uh from the data preparation uh download things always takes time right and uh tend to fail due to the network uh solution and also we need to deal with different kinds of data data source And also we have the data governance requirement in the enterprise.

We need to share things uh across different group teams or different name spaces and also we need to deal with the virtual version control and uh reproduce ability things. So uh one typical dark moment for our uh AI engineer is it was working on my machine but not here right. Look at those uh error messages. I believe some of them you familiar with them. So it was on my machine. It was on my machine. Uh do you think this term familiar to you? 10 years ago, more than 10 years ago, Docker was born to address this term, right? So, most of you may ask why not using Docker image to manage all of those dependencies, all those Python dependencies. Um, you can just do a uh do a math. Um we have a lot of layers from the system library to the CUDA to the Python to the uh PyTorch to the transformer and a lot of the uh libraries. So um you have you can do the uh preparation and combination the those things together the docker image amount will become a aonomic huge lumber. So uh so you will it's not very suitable to use docker to handle all of this.

So after you doing your hard work you have tidy all the python dependency in your developer environment. But when we shift from the developer environment to the uh training and then to the influence it's not wasting of time to reinstall them. But also the worst nightmare is the dependency uh will will drift the dependency relationship will uh break from here to there. So we do need a solution one solution which we define
