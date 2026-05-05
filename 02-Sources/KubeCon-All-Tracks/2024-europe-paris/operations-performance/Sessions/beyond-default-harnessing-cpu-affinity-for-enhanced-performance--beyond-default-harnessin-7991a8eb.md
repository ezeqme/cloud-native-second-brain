---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2024 - Paris, France"
event_id: kccnceu2024
year: 2024
region: "Europe"
city: "Paris"
country: "France"
event_date: "2024-03-19/2024-03-22"
track: "Operations + Performance"
themes: ["SRE Reliability"]
speakers: ["Antti Kervinen", "Intel", "Dixita Narang", "Google LLC"]
sched_url: https://kccnceu2024.sched.com/event/1YeMY/beyond-default-harnessing-cpu-affinity-for-enhanced-performance-across-your-workload-portfolio-antti-kervinen-intel-dixita-narang-google-llc
youtube_search_url: https://www.youtube.com/results?search_query=Beyond+Default%3A+Harnessing+CPU+Affinity+for+Enhanced+Performance+Across+Your+Workload+Portfolio+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Beyond Default: Harnessing CPU Affinity for Enhanced Performance Across Your Workload Portfolio - Antti Kervinen, Intel & Dixita Narang, Google LLC

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[Operations + Performance]]
- Temas: [[SRE Reliability]]
- País/cidade: France / Paris
- Speakers: Antti Kervinen, Intel, Dixita Narang, Google LLC
- Schedule: https://kccnceu2024.sched.com/event/1YeMY/beyond-default-harnessing-cpu-affinity-for-enhanced-performance-across-your-workload-portfolio-antti-kervinen-intel-dixita-narang-google-llc
- Busca YouTube: https://www.youtube.com/results?search_query=Beyond+Default%3A+Harnessing+CPU+Affinity+for+Enhanced+Performance+Across+Your+Workload+Portfolio+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Beyond Default: Harnessing CPU Affinity for Enhanced Performance Across Your Workload Portfolio.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1YeMY/beyond-default-harnessing-cpu-affinity-for-enhanced-performance-across-your-workload-portfolio-antti-kervinen-intel-dixita-narang-google-llc
- YouTube search: https://www.youtube.com/results?search_query=Beyond+Default%3A+Harnessing+CPU+Affinity+for+Enhanced+Performance+Across+Your+Workload+Portfolio+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=h3HY0kSh8s4
- YouTube title: Beyond Default: Harnessing CPU Affinity for Enhanced Performance Across Your Workload Portfolio
- Match score: 1.08
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/beyond-default-harnessing-cpu-affinity-for-enhanced-performance-across/h3HY0kSh8s4.txt
- Transcript chars: 28431
- Keywords: balloon, containers, policy, balloons, container, actually, workloads, running, already, default, workload, manager, memory, policies, topology, performance, device, runtime

### Resumo baseado na transcript

today Dixie and myself Auntie are going to talk about CPU Affinity that means that which set of CPUs should run which set of containers why it makes a big difference and how you can actually do it so when we already got our presentation accepted I asked Dixie if she had some like relevant work Lo in mind with which we could demonstrate the benefits of CPU Affinity she provided me with the docker file for running tensor flow AI model training on CPU and we had a note

### Excerpt da transcript

today Dixie and myself Auntie are going to talk about CPU Affinity that means that which set of CPUs should run which set of containers why it makes a big difference and how you can actually do it so when we already got our presentation accepted I asked Dixie if she had some like relevant work Lo in mind with which we could demonstrate the benefits of CPU Affinity she provided me with the docker file for running tensor flow AI model training on CPU and we had a note kuus worker note uh with this kind of Hardware maybe it's not sorry maybe it's not fully visible uh there but it's like a two socket system having 128 CPUs in it and operating system was telling that okay there are two new man noes here like one CPU for one Numan node the other CPU for the other Numan node and when we went to the bias and enabled subn Numa clustering uh then more details about this Hardware was exposed to the operating system and it resulted in showing that you have eight Numa noes so eight set of CPUs eight memories and that's something which makes a difference when we are assigning workload to these CPUs so what I'm presenting here is a um throughput from that AI model training when we are increasing the number of containers on that node that are doing the training in parallel so in the beginning we are running just a single container and there is no big difference in the throughputs in these three cases so one case is we do not have any CPU Affinity at all the other one is that we are assigning these containers to a set of four CPUs each finally there's a case with running a container on only two two CPUs for each container and when we were adding more containers on this note already there's a big difference now when we are running eight containers that is eight trainings concurrently so line for no CPU affinity and then top lines for two and four CPUs and when increasing the number of containers again now up to 15 containers running in parallel the chomp is pretty clear when we are doing CPU Affinity setting there and if there is no CPU Affinity that is all tensor flow trainings can see all the CPS on the Note then this doesn't really increase through but that much and finally when pushing to the limits we are running 20 containers simultaneously there on the Note uh when I tried to push even more that resulted in out of memory error so we do not have just enough memory for that purpose this time um but there we can see now maybe a small difference between two CPUs and four
