---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2024 - Paris, France"
event_id: kccnceu2024
year: 2024
region: "Europe"
city: "Paris"
country: "France"
event_date: "2024-03-19/2024-03-22"
track: "Project Opportunities"
themes: ["AI ML", "Kubernetes Core", "Sustainability"]
speakers: []
sched_url: https://kccnceu2024.sched.com/event/1aQWg/sustainable-computing-measuring-application-energy-consumption-in-kubernetes-environments-with-kepler-project-lightning-talk
youtube_search_url: https://www.youtube.com/results?search_query=Sustainable+Computing%3A+Measuring+Application+Energy+Consumption+in+Kubernetes+Environments+with+Kepler+%7C+Project+Lightning+Talk+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Sustainable Computing: Measuring Application Energy Consumption in Kubernetes Environments with Kepler | Project Lightning Talk

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[Project Opportunities]]
- Temas: [[AI ML]], [[Kubernetes Core]], [[Sustainability]]
- País/cidade: France / Paris
- Speakers: N/A
- Schedule: https://kccnceu2024.sched.com/event/1aQWg/sustainable-computing-measuring-application-energy-consumption-in-kubernetes-environments-with-kepler-project-lightning-talk
- Busca YouTube: https://www.youtube.com/results?search_query=Sustainable+Computing%3A+Measuring+Application+Energy+Consumption+in+Kubernetes+Environments+with+Kepler+%7C+Project+Lightning+Talk+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Sustainable Computing: Measuring Application Energy Consumption in Kubernetes Environments with Kepler | Project Lightning Talk.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1aQWg/sustainable-computing-measuring-application-energy-consumption-in-kubernetes-environments-with-kepler-project-lightning-talk
- YouTube search: https://www.youtube.com/results?search_query=Sustainable+Computing%3A+Measuring+Application+Energy+Consumption+in+Kubernetes+Environments+with+Kepler+%7C+Project+Lightning+Talk+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=7_a9mCTcxkk
- YouTube title: Sustainable Computing: Measuring Application Energy Consumption in Kubernetes Environments with K...
- Match score: 0.953
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/sustainable-computing-measuring-application-energy-consumption-in-kube/7_a9mCTcxkk.txt
- Transcript chars: 5362
- Keywords: energy, consumption, kepler, resource, utilization, models, process, components, gpu, application, aggregate, updates, introduce, collect, database, report, trainings, everyone

### Resumo baseado na transcript

hello everyone so we're going to present today the Kepler uh updates Kepler is a cncf and BOS project um we are one of the main developers of Kepler uh I'm Marcel moral and she's San also known as Pang we are from IBM research in Tokyo and we are have been contributing to the capler development for a few years so we'll start just you know with some uh quick introduction what scaper is for the ones that doesn't know and the main updates uh apart from you know

### Excerpt da transcript

hello everyone so we're going to present today the Kepler uh updates Kepler is a cncf and BOS project um we are one of the main developers of Kepler uh I'm Marcel moral and she's San also known as Pang we are from IBM research in Tokyo and we are have been contributing to the capler development for a few years so we'll start just you know with some uh quick introduction what scaper is for the ones that doesn't know and the main updates uh apart from you know bug fix and performance improvements we have some um key uh updates for this year then we're going to introduce in this short talk so first of all what's Kepler Kepler is a project to measure the energy consumption of process and then aggregated to container spot and other Gres so basically there is no way to measure the energy consumption of process direct to the hardware there's no counters for that but we have the energy consumption of components for example CPU energy consumption and the energy consumption is directly related to the resource utilization so by having the resource utilization of process and the energy consumption of components we do the calculation and what's the proportional energy us that was used by some specific process um to collect the resource utilization we use the BPF that is a light uh um that introduce low overhead to get the restor utilization for process and for system like that there is no of access to the hardware sensors that shows the energy consumption uh of of components we like virtual machines on public Cloud we use pre-trained power power models that are par models that are being trained collecting the energy consumption of um of some resource and resource utilization in some specific bare metal node sorry uh we export all this information to perms and then we have also gra dashboards that can V visualize the energy consumption of the components of the application components um the new feature that we have right now is support for uh um GPU virtualization more specifically for the Mig features that is Li the GPU in different uh partitions so the GPU uh M the N Mig feature does not show the energy consumption per slice it's the energy consumption for the entire GPU so that we need power models also for that so uh in this case we collect the power consumption of the entire GPU we get the resource utilization of each slice and partition this energy consumption between these lies and then associate that to the process that are running on these lies um well the resou
