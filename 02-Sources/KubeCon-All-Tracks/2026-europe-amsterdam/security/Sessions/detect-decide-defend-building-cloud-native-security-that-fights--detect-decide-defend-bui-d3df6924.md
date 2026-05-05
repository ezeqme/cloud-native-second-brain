---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Security"
themes: ["Security"]
speakers: ["Matthias Bertschy", "ARMO"]
sched_url: https://kccnceu2026.sched.com/event/2CW3S/detect-decide-defend-building-cloud-native-security-that-fights-back-matthias-bertschy-armo
youtube_search_url: https://www.youtube.com/results?search_query=Detect%2C+Decide%2C+Defend%3A+Building+Cloud+Native+Security+That+Fights+Back+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Detect, Decide, Defend: Building Cloud Native Security That Fights Back - Matthias Bertschy, ARMO

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Security]]
- Temas: [[Security]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Matthias Bertschy, ARMO
- Schedule: https://kccnceu2026.sched.com/event/2CW3S/detect-decide-defend-building-cloud-native-security-that-fights-back-matthias-bertschy-armo
- Busca YouTube: https://www.youtube.com/results?search_query=Detect%2C+Decide%2C+Defend%3A+Building+Cloud+Native+Security+That+Fights+Back+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Detect, Decide, Defend: Building Cloud Native Security That Fights Back.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2CW3S/detect-decide-defend-building-cloud-native-security-that-fights-back-matthias-bertschy-armo
- YouTube search: https://www.youtube.com/results?search_query=Detect%2C+Decide%2C+Defend%3A+Building+Cloud+Native+Security+That+Fights+Back+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=5DxaxeWNkYY
- YouTube title: Detect, Decide, Defend: Building Cloud Native Security That Fights Back - Matthias Bertschy, ARMO
- Match score: 0.935
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/detect-decide-defend-building-cloud-native-security-that-fights-back/5DxaxeWNkYY.txt
- Transcript chars: 13794
- Keywords: application, profile, native, detection, workload, happened, attack, behavior, another, create, security, incident, baseline, already, remediation, process, signals, normal

### Resumo baseado na transcript

So when you are uh on call and your your day starts like this, you know it's going to be fun. A change detection workload in your EKS cluster just spawned a reverse shell. So we should build this baseline and it can be derived from Kubernetes metadata. Then some commands are executed it and at the end we learn what the system is with you name. Um then some some manipulation in the different kubernetes uh resources and finally something happened in in AWS. the allowed process, the allowed C calls, what are the network destinations, which file system parts you can access, what are the security posture expectations.

### Excerpt da transcript

Welcome to this talk. So when you are uh on call and your your day starts like this, you know it's going to be fun. So let's take an example. A change detection workload in your EKS cluster just spawned a reverse shell. Oh my god, what happened? So the problem uh with the security in Kubernetes is that it's layered. So you have a web application firewall and it sees an injection. You have an ebpf uh probe that sees a process execution. your Kubernetes sees some API calls and then you have some cloud security that sees some IM activity. Problem is when you get a security incident, it doesn't respect the layers. So we have four tools, four different alerts, but nobody understand what's going on or what happened. So I'm here to show you a framework on how to make it better. My name is Matias. I'm a developer for the a company called Armo. We do Kubernetes security. I'm a CNCF maintainer of three projects, Cubscape, Pro, and Inspector Gadget. And I've been contributing to Kubernetes since 2016. If you used startup probes, that's some of my work.

And if you ever wondered why the native sidecars they are in it containers, that's also my fault. So we can talk together after if you don't like it. Um so the real problem is we don't lack signal. We don't we we have enough signals but we lack a connected understanding as I said before like each layer sees its own information. So SQL injection we have like a Python 3 that has spawned a bash communities API as I said the cloud IM and if you take all these incident it could be just noise but if you connect the dots you understand that it's a real attack. So how do we move from disconnected events to a coherent incident story? So first of all we need to define what normal means you know so every cloud native workload has a predictable behavior uh that's what we call the baseline behavior it includes the expected processes uh the network behavior what are the system calls which files are accessed which files are open executed what airbach uh rules are being used. So if if you know what the normal for your application looks like uh the detection can be really improved.

So we should build this baseline and it can be derived from Kubernetes metadata. It could be derived from EVPF probes signals and ideally we should like store them in a cloud native format. So I suggest we call this an application profile and let's make it a CRD. So what happens when the runtime behavior breaks that baseline when it's out of the normal? So
