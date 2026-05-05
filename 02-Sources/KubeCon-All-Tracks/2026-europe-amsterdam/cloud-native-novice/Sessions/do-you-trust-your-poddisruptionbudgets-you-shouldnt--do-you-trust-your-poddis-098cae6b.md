---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Cloud Native Novice"
themes: ["Cloud Native Novice"]
speakers: ["Kārlis Akots Gribulis", "Saxo Bank"]
sched_url: https://kccnceu2026.sched.com/event/2CVyu/do-you-trust-your-poddisruptionbudgets-you-shouldnt-karlis-akots-gribulis-saxo-bank
youtube_search_url: https://www.youtube.com/results?search_query=Do+You+Trust+Your+PodDisruptionBudgets%3F+You+Shouldn%E2%80%99t%21+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Do You Trust Your PodDisruptionBudgets? You Shouldn’t! - Kārlis Akots Gribulis, Saxo Bank

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Cloud Native Novice]]
- Temas: [[Cloud Native Novice]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Kārlis Akots Gribulis, Saxo Bank
- Schedule: https://kccnceu2026.sched.com/event/2CVyu/do-you-trust-your-poddisruptionbudgets-you-shouldnt-karlis-akots-gribulis-saxo-bank
- Busca YouTube: https://www.youtube.com/results?search_query=Do+You+Trust+Your+PodDisruptionBudgets%3F+You+Shouldn%E2%80%99t%21+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Do You Trust Your PodDisruptionBudgets? You Shouldn’t!.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2CVyu/do-you-trust-your-poddisruptionbudgets-you-shouldnt-karlis-akots-gribulis-saxo-bank
- YouTube search: https://www.youtube.com/results?search_query=Do+You+Trust+Your+PodDisruptionBudgets%3F+You+Shouldn%E2%80%99t%21+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=yRc4yr7CQh4
- YouTube title: Do You Trust Your PodDisruptionBudgets? You Shouldn’t! - Kārlis Akots Gribulis, Saxo Bank
- Match score: 0.841
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/do-you-trust-your-poddisruptionbudgets-you-shouldnt/yRc4yr7CQh4.txt
- Transcript chars: 22844
- Keywords: priority, disruption, delete, suddenly, eviction, budget, default, voluntary, against, higher, cannot, meaning, scenarios, ignore, update, command, request, quality

### Resumo baseado na transcript

It's nice to see so many people interested about pod disruption budgets. I've previously built Kubernetes clusters for companies such as Accenture and Vox and I sometimes get bored and collect too many uh certificates. What did you do?" I'm like, I I didn't even touch Prometheus and I see the pod is down. time the PDB is invalid then and Yeah, it's meant to keep your applications more stable and keep them more highly available in your environment in a disruptive environment because Kubernetes by default is a disruptive environment. If you have maybe hypervisor fails either be it on your Windows machines or other platforms like VM and so on if there's error on that side it will also the node and the hypervisor will have issues and kubernetes cannot prevent issues uh on monthly continuity tests where we basically network-wise disconnect one data center out and just see what happens everything should still work and in those scenarios we can see that you know all the pods are unreachable and then by default Kubernetes could only within five

### Excerpt da transcript

It's nice to see so many people interested about pod disruption budgets. Although I thought everyone knew knew about that. But let's start about me. I'm Carlo Sakos Gribbles. I'm from RIA Latvia but currently I'm working for Saxabank. So I'm living in Denmark. I've previously built Kubernetes clusters for companies such as Accenture and Vox and I sometimes get bored and collect too many uh certificates. So quickly about Saxo Bank just so you have some context. The company was founded in 1992. It has 100 uh billion USD client assets, one and a half million clients, 70,000 financial instruments, and it's been designated a CFI bank, which means some say it's too big to fail. From my point of view, it's I should not fail otherwise I'm in big trouble. So as a container platform engineer, I I do containers, I do updates and as many of you probably make some platform changes. You bump some resources and uh some of you have maybe the assumed safety of PDB. That's something that I had before. But then on a regular platform maintenance evening, you know, I'm just doing my bumps.

I'm updating English, updating other controllers. And then suddenly I get a call from a manager 10 minutes later asking, "Hey, there's no metrics anymore. What did you do?" I'm like, I I didn't even touch Prometheus and I see the pod is down. There's no metrics coming in. So, the English kind of kicked it out and then we started to figure out, okay, what's going on? Why did it happen? How can we prevent it in the future? And so on. And at that point, uh PDBs felt like a nice Swiss cheese. It's, you know, it's nice, but it has a lot of holes. So many things can go through it and you have to be aware of all the rules within it. So for those who don't know as this is a cloud native novice track what is a PDB if you would ask you know our lovely AIS this is what it would generate for you which you know it kind of highlights it mostly what it is yeah it protects pods it has uh only two settings which is minimum available or maximum unavailable although I only hope it actually meant that you can select one of those two not both because that's you cannot select both at the same time the PDB is invalid then and Yeah, it's meant to keep your applications more stable and keep them more highly available in your environment in a disruptive environment because Kubernetes by default is a disruptive environment.

And uh this is a line I also got from the Kubernetes documentations. I also highlighted it be
