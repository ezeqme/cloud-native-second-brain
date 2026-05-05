---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom"
event_id: kccnceu2025
year: 2025
region: "Europe"
city: "London"
country: "United Kingdom"
event_date: "2025-04-01/2025-04-04"
track: "Emerging + Advanced"
themes: ["Runtime Containers", "Kubernetes Core"]
speakers: ["Dejan Pejchev", "Jonathan Giannuzzi", "G-Research"]
sched_url: https://kccnceu2025.sched.com/event/1txFP/get-witty-evolving-kubernetes-scheduling-with-the-webassembly-component-model-dejan-pejchev-jonathan-giannuzzi-g-research
youtube_search_url: https://www.youtube.com/results?search_query=Get+WITty%3A+Evolving+Kubernetes+Scheduling+With+the+WebAssembly+Component+Model+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Get WITty: Evolving Kubernetes Scheduling With the WebAssembly Component Model - Dejan Pejchev & Jonathan Giannuzzi, G-Research

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Emerging + Advanced]]
- Temas: [[Runtime Containers]], [[Kubernetes Core]]
- País/cidade: United Kingdom / London
- Speakers: Dejan Pejchev, Jonathan Giannuzzi, G-Research
- Schedule: https://kccnceu2025.sched.com/event/1txFP/get-witty-evolving-kubernetes-scheduling-with-the-webassembly-component-model-dejan-pejchev-jonathan-giannuzzi-g-research
- Busca YouTube: https://www.youtube.com/results?search_query=Get+WITty%3A+Evolving+Kubernetes+Scheduling+With+the+WebAssembly+Component+Model+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Get WITty: Evolving Kubernetes Scheduling With the WebAssembly Component Model.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1txFP/get-witty-evolving-kubernetes-scheduling-with-the-webassembly-component-model-dejan-pejchev-jonathan-giannuzzi-g-research
- YouTube search: https://www.youtube.com/results?search_query=Get+WITty%3A+Evolving+Kubernetes+Scheduling+With+the+WebAssembly+Component+Model+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=hjbZOBghxYU
- YouTube title: Get WITty: Evolving Kubernetes Scheduling With the WebAssembly... Dejan Pejchev & Jonathan Giannuzzi
- Match score: 0.864
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/get-witty-evolving-kubernetes-scheduling-with-the-webassembly-componen/hjbZOBghxYU.txt
- Transcript chars: 22957
- Keywords: component, filter, plug-in, write, function, actually, assembly, basically, generate, pretty, scheduleuler, string, memory, language, extension, complex, schema, everybody

### Resumo baseado na transcript

Uh I so I hope everybody's uh interested for yet another web assembly component model talk. So um today what we wanted to do is uh we want to show you our journey where we wanted to apply the component model to the Kubernetes scheduler. Just just for the other ones very briefly, uh Web Assembly, it's portable across architectures, you know, ARM, Intel, etc. You've got your Kubernetes scheduleuler and this time you deploy the super cool cube scheduleuler WASOM extension which is a mouthful uh as a framework plug-in. Uh we can describe our structures the complex Kubernetes structures like uh for a pod for a node. So and especially when sharing complex structures one major challenge arises.

### Excerpt da transcript

So hello everybody. Uh I so I hope everybody's uh interested for yet another web assembly component model talk. Ah okay. Yeah that's the enthusiasm. I'm a bit surprised. Nice. So um today what we wanted to do is uh we want to show you our journey where we wanted to apply the component model to the Kubernetes scheduler. So my name is Dan Pchev. I'm an open source engineer with the G research open source team. So together with my colleague we'll try to walk you through our journey uh through the road bumps we encountered. So Jonathan if you may. Yeah. So hi everyone. I'm Jonathan. I also work for G Research in the open source team and I work on all kinds of things uh that are open source in pretty much any programming language and always with a focus on performance and maintainability. And so first I want to do a little previously in episode one of Diane and Yonathan Jonathan go to CubeCon. So back then we discussed the magic behind the Kubernetes scheduleuler uh and the various ways that you can extend it.

If if you are interested in this and you missed it the last time when we were in Salt Lake City, I would highly recommend you go ahead and watch our talk uh but not right now obviously just half an hour uh because we're not going to talk about it in more details now. I'm just going to try you to to try to give you enough context to appreciate the next 25 minutes hopefully. Um, so last time we looked at the wholeuling cycle and all the places where you can hook your own code into it and there's, as you can see on that picture, there's quite a few. And then we explore the three ways that you can uh hook your code into that. So one of them is the schedule extenders, which is basically web hooks. You can write this in any language and it's just JSON over HTTP. Obviously, you'll have a fairly high latency because it goes over the network and there's only just four places you can extend that. This is basically legacy stuff. Um, the other one is theuling framework plugins. That is like the big boy stuff where your code ends up being part of the scheduleuler itself.

Um, and you have to deploy a custom binary uh of the scheduleuler plus your code. that is super efficient because you're completely uh entirely native Go code but that's not very flexible in terms of deployments and also there's more than a dozen extension points basically all the ones you saw in the previous slide so you can really go crazy in terms of implementing your own custom logic and then fi
