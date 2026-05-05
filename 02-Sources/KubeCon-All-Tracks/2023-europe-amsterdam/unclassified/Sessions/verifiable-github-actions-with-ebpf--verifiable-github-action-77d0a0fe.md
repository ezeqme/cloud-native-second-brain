---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands"
event_id: kccnceu2023
year: 2023
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2023-04-17/2023-04-21"
track: "Unclassified"
themes: ["Cloud Native"]
speakers: ["Jose Donizetti", "Aqua"]
sched_url: https://kccnceu2023.sched.com/event/1HybH/verifiable-github-actions-with-ebpf-jose-donizetti-aqua
youtube_search_url: https://www.youtube.com/results?search_query=Verifiable+GitHub+Actions+with+eBPF+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Verifiable GitHub Actions with eBPF - Jose Donizetti, Aqua

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands
- Trilha oficial: [[Unclassified]]
- Temas: [[Cloud Native]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Jose Donizetti, Aqua
- Schedule: https://kccnceu2023.sched.com/event/1HybH/verifiable-github-actions-with-ebpf-jose-donizetti-aqua
- Busca YouTube: https://www.youtube.com/results?search_query=Verifiable+GitHub+Actions+with+eBPF+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Verifiable GitHub Actions with eBPF.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2023.sched.com/event/1HybH/verifiable-github-actions-with-ebpf-jose-donizetti-aqua
- YouTube search: https://www.youtube.com/results?search_query=Verifiable+GitHub+Actions+with+eBPF+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=6vNt9JMU9p4
- YouTube title: Verifiable GitHub Actions with eBPF - Jose Donizetti, Aqua
- Match score: 0.858
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/verifiable-github-actions-with-ebpf/6vNt9JMU9p4.txt
- Transcript chars: 23043
- Keywords: profile, create, github, process, activity, trace, signatures, actually, executions, action, events, binary, change, whenever, baseline, workflow, attack, collect

### Resumo baseado na transcript

thank you for coming I'm just there I will I'm an open source engineer at Alpha security this talk was great with ikai he runs the open source team at Aqua today you'll be presenting by myself just some context like a couple years ago some very meaningful attacks opens like everyone's eyes First Supply Chain secure right the code called attack for example an attacker was able to modify their bash script the installer so whenever you were installing kodakov this would collect like sensitive information and send you

### Excerpt da transcript

thank you for coming I'm just there I will I'm an open source engineer at Alpha security this talk was great with ikai he runs the open source team at Aqua today you'll be presenting by myself just some context like a couple years ago some very meaningful attacks opens like everyone's eyes First Supply Chain secure right the code called attack for example an attacker was able to modify their bash script the installer so whenever you were installing kodakov this would collect like sensitive information and send you a remote IP right so if you were using GitHub actions for example whenever you're installing the code call of action it would collect your GitHub token and send to this remote IP uh like all others we also want to like explore a solution for this and we start a POC for GitHub action specifically but our perspective were like runtime security right we want to try to bring the word of runtime security to attempt to fix this problem uh and that that's what what I want to talk to you like in this talk right the POC we did the attempts we did were implemented and a few things we learned along the way uh why runtime security because that's what we do right I work on the Tracy project it's an open source project for runtime security and forensics Tracy will use ebpf to collect events on your kernel over 500 of those events right like so it's a lot of Evans and those errors can be as simple as assist call so you can say I want to know whenever the righteous call happens the host or I want to know if a specific process is doing a right Cisco right but there are also like Complex events which we call like Signature Events right those complex drives the idea that they detect malicious activity so you can ask Tracy to trig an event if a violence attack is happening on the host or a reverse shell right uh when you have a hammer everything looks like a nail and traces are Hammer so that's why we want to try to use to fix this problem with supply chain uh the first solution we attempt was pretty basic we got Tracy the way it was with its signature servant we brought we create a GitHub action right we had a trace to it so whenever someone would use it Trace would boot in the background and see if any malicious activity what's happening um it was actually like good to see this working because we didn't know at first if we would be able to run a BPF in GitHub actions and it did work uh was a good first step but first lesson comes uh right after the the release of
