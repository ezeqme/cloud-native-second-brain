---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States"
event_id: kccncna2024
year: 2024
region: "North America"
city: "Salt Lake City"
country: "United States"
event_date: "2024-11-12/2024-11-15"
track: "Emerging + Advanced"
themes: ["Runtime Containers", "Kubernetes Core", "SRE Reliability"]
speakers: ["Dejan Pejchev", "Jonathan Giannuzzi", "G-Research"]
sched_url: https://kccncna2024.sched.com/event/1i7p8/wasm-+-kwok-wizardry-writing-and-testing-scheduler-plugins-at-scale-dejan-pejchev-jonathan-giannuzzi-g-research
youtube_search_url: https://www.youtube.com/results?search_query=WASM+%2B+KWOK+Wizardry%3A+Writing+and+Testing+Scheduler+Plugins+at+Scale+CNCF+KubeCon+2024
slides: []
status: parsed
---

# WASM + KWOK Wizardry: Writing and Testing Scheduler Plugins at Scale - Dejan Pejchev & Jonathan Giannuzzi, G-Research

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[Emerging + Advanced]]
- Temas: [[Runtime Containers]], [[Kubernetes Core]], [[SRE Reliability]]
- País/cidade: United States / Salt Lake City
- Speakers: Dejan Pejchev, Jonathan Giannuzzi, G-Research
- Schedule: https://kccncna2024.sched.com/event/1i7p8/wasm-+-kwok-wizardry-writing-and-testing-scheduler-plugins-at-scale-dejan-pejchev-jonathan-giannuzzi-g-research
- Busca YouTube: https://www.youtube.com/results?search_query=WASM+%2B+KWOK+Wizardry%3A+Writing+and+Testing+Scheduler+Plugins+at+Scale+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre WASM + KWOK Wizardry: Writing and Testing Scheduler Plugins at Scale.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1i7p8/wasm-+-kwok-wizardry-writing-and-testing-scheduler-plugins-at-scale-dejan-pejchev-jonathan-giannuzzi-g-research
- YouTube search: https://www.youtube.com/results?search_query=WASM+%2B+KWOK+Wizardry%3A+Writing+and+Testing+Scheduler+Plugins+at+Scale+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=O-cFJJYZkcs
- YouTube title: WASM + KWOK Wizardry: Writing and Testing Scheduler Plugins at Scale - D. Pejchev, J. Giannuzzi
- Match score: 0.935
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/wasm-kwok-wizardry-writing-and-testing-scheduler-plugins-at-scale/O-cFJJYZkcs.txt
- Transcript chars: 27053
- Keywords: plugins, plugin, scheduler, scheduling, wasm, filter, simulator, actually, plug-in, create, annotation, framework, resources, wizards, schuler, return, jonathan, control

### Resumo baseado na transcript

I'd like to thank you all for joining this talk so my name is Dan pev I'm an open source software engineer or in the spirit of this stock I'm an open source Wizard and we are part of the g- research open source team where our responsibility is to spread the good word of Open Source and contribute back to the amazing communities which build such awesome projects so today we'll look and demystify a lot of magic around the cube scheduler around web assembly we'll try to build

### Excerpt da transcript

I'd like to thank you all for joining this talk so my name is Dan pev I'm an open source software engineer or in the spirit of this stock I'm an open source Wizard and we are part of the g- research open source team where our responsibility is to spread the good word of Open Source and contribute back to the amazing communities which build such awesome projects so today we'll look and demystify a lot of magic around the cube scheduler around web assembly we'll try to build some Cube schu plugins using different Frameworks different toolings uh see how we can test that at scale and yeah handing over to my colleague who is actually a grand visard of Sir so Jonathan to you thank you danan uh hello everyone hello cucon uh I'm Jonathan janzi I also work for G research based in London and in my role on open source team done all kinds of Witchcraft from speeding up net runtime startup on Apple silicon Max from uh solving caching issues in dock bkit or more recently building a machine learning experiment tracker to support complex research workflows but uh today I'm not here to discuss any of that instead D Diane and I are excited to share some kubernetes Wizardry so let's get ready for a wasm and kubernetes journey filled with enchantment and it all starts with the mysterious kubernetes scheduler the kubernetes scheduler is an essential control plane component of the kues cluster it's responsible for determining which pods sorry which nodes in the cluster should run the newly created pods and it's taking for it's taking into account each pod's resource requirements like the CPU the memory and also the current state of the nodes it will go and care evaluate constraints and resource availability to select the most suitable node for a pod it's almost like casting a careful placement spell Additionally the scheduler manages preemption by ident identifying and removing lower priority pods from nodes where there aren't enough resources available for the higher priority pods to run now let's dive into the enchanting sheduling life cycle and see how it all unfolds so the sheduling life cycle will involve several phases to manage the pot placement efficiently and fairly we'll work through these phases in order from left to right there's the first group which is queuing then sheduling then binding in the queuing group we start with pre and Q this is before pods that enter the sheding queue the scheduler can already filter them this will ensure that only the eligible and pr
