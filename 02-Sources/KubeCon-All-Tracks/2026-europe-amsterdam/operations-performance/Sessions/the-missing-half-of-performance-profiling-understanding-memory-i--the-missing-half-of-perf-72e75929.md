---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Operations + Performance"
themes: ["Observability", "SRE Reliability"]
speakers: ["Dom Delnano", "Cosmic"]
sched_url: https://kccnceu2026.sched.com/event/2CW2d/the-missing-half-of-performance-profiling-understanding-memory-in-cloud-native-systems-dom-delnano-cosmic
youtube_search_url: https://www.youtube.com/results?search_query=The+Missing+Half+of+Performance+Profiling%3A+Understanding+Memory+in+Cloud+Native+Systems+CNCF+KubeCon+2026
slides: []
status: parsed
---

# The Missing Half of Performance Profiling: Understanding Memory in Cloud Native Systems - Dom Delnano, Cosmic

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Operations + Performance]]
- Temas: [[Observability]], [[SRE Reliability]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Dom Delnano, Cosmic
- Schedule: https://kccnceu2026.sched.com/event/2CW2d/the-missing-half-of-performance-profiling-understanding-memory-in-cloud-native-systems-dom-delnano-cosmic
- Busca YouTube: https://www.youtube.com/results?search_query=The+Missing+Half+of+Performance+Profiling%3A+Understanding+Memory+in+Cloud+Native+Systems+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre The Missing Half of Performance Profiling: Understanding Memory in Cloud Native Systems.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2CW2d/the-missing-half-of-performance-profiling-understanding-memory-in-cloud-native-systems-dom-delnano-cosmic
- YouTube search: https://www.youtube.com/results?search_query=The+Missing+Half+of+Performance+Profiling%3A+Understanding+Memory+in+Cloud+Native+Systems+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=rTkrS46meSM
- YouTube title: The Missing Half of Performance Profiling: Understanding Memory in Cloud Native Syste... Dom Delnano
- Match score: 1.014
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/the-missing-half-of-performance-profiling-understanding-memory-in-clou/rTkrS46meSM.txt
- Transcript chars: 22867
- Keywords: memory, profiling, sampling, allocated, program, actually, allocation, overhead, allocations, function, available, tooling, container, performance, provide, basically, distribution, support

### Resumo baseado na transcript

Thank you for joining me today and I'm excited to share more about the missing half of performance profiling, understanding memory in cloudnative systems. Before we jump into things, I wanted to give myself a brief introduction. I'm sure we've all had that experience where Sophos or some security scanning software runs on your computer or you run something expensive, your fan kicks on, the Mac spinning pin wheel shows up and your computer grinds to a halt and you're left with what's going on. As any good engineer, what this forced us to do was form the uh area of performance profiling and specifically we started kind of in the CPU profiling area. I'm sure many of you have seen an issue like this before where your Kubernetes pods are running just fine and then memory usage continues to creep up and then all of a sudden they hit the pod limit and Linux kills the processes. Um and then there's also in use metrics which are basically like the net from what you've allocated against what you've deallocated.

### Excerpt da transcript

Hello CubeCon. Thank you for joining me today and I'm excited to share more about the missing half of performance profiling, understanding memory in cloudnative systems. Before we jump into things, I wanted to give myself a brief introduction. For the last six years, I've been working in the ebpf space. Um, most of that focused on the CNCF Pixie project, which does observability for Kubernetes. Um, I've also worked at CrowdStrike and some other companies uh applying EBPF in other areas as well. My day job is working as an engineer at a startup called Gimlet Labs where we're building the first multisilicon AI inference cloud. Um, and you can find me at my socials on this slide. Since the beginning of time, computing's oldest enemy has been debugging slow programs. In the early days in the 1960s, you would take your punch cards, give them over to the operator. The operator would then run your program at some point in the future. Hours or days later, you would get the print out. And if there were issues there, you know, you'd then have to debug and figure out what was going on.

Moving on to the days of personal computing. I'm sure we've all had that experience where Sophos or some security scanning software runs on your computer or you run something expensive, your fan kicks on, the Mac spinning pin wheel shows up and your computer grinds to a halt and you're left with what's going on. And even today, despite all the sophistication in the modern cloud environments, with how distributed and complex things have gotten, a timeout error like this is often extremely challenging to debug. There's so many areas to look at. And so, despite our software getting more and more complex, slow programs have always been something that's been challenging. As any good engineer, what this forced us to do was form the uh area of performance profiling and specifically we started kind of in the CPU profiling area. So looking back to the 1980s and 1990s, we had this tool called GPRO. It worked at the scope of a single program. The way you instrumented the program was through recompiling it.

You'd have to provide this -pg flag. This was done ad hoc since you had to recompile the program and the way the instrumentation worked it actually, you know, added a whole bunch of stuff to the binary and so the overhead was very high. Moving on to the 2000s and 2010s, uh, sampling profilers became a thing. Tools like Perf. This changed the scope of these profilers from a single program to a
