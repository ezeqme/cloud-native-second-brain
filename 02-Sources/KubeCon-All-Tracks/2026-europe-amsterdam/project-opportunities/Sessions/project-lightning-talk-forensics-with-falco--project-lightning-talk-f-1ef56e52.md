---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Project Opportunities"
themes: ["AI ML", "Community Governance"]
speakers: ["Gerald Combs", "Maintainer"]
sched_url: https://kccnceu2026.sched.com/event/2EFx1/project-lightning-talk-forensics-with-falco-gerald-combs-maintainer
youtube_search_url: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Forensics+With+Falco+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Project Lightning Talk: Forensics With Falco - Gerald Combs, Maintainer

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Project Opportunities]]
- Temas: [[AI ML]], [[Community Governance]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Gerald Combs, Maintainer
- Schedule: https://kccnceu2026.sched.com/event/2EFx1/project-lightning-talk-forensics-with-falco-gerald-combs-maintainer
- Busca YouTube: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Forensics+With+Falco+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Project Lightning Talk: Forensics With Falco.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2EFx1/project-lightning-talk-forensics-with-falco-gerald-combs-maintainer
- YouTube search: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Forensics+With+Falco+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=oiuh1eHGFMY
- YouTube title: Project Lightning Talk: Forensics With Falco - Gerald Combs, Maintainer
- Match score: 0.862
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/project-lightning-talk-forensics-with-falco/oiuh1eHGFMY.txt
- Transcript chars: 5156
- Keywords: capture, default, stratark, wireshark, engine, analysis, actually, enable, gerald, messages, triggers, investigative, called, normally, around, cubecon, configuration, screen

### Resumo baseado na transcript

Uh I'm more well known as the creator and lead developer of Wireshark, but I am also a Falco maintainer. Uh first of all, Falco, if you're not familiar with it, it is a cloudnative real-time threat detection engine. Now, last year at CubeCon North America, I gave a demo of using Stratark with Falco and um I I focused mainly on the Stratark side and and I finished up the talk showing that the that you can actually use these tools to look at data that was transmitted across a pipe. Um now for the demo that I did last fall, I actually had to enable a bit more information. And this is something you might want to if you want to play with, you might want to take care because you can run into something called the observer effect where if you're monitoring a system, you can affect the performance of that system. Um, I know in the nubbing world where I come from, you can kind of throw money at this problem and and buy passive hardware taps.

### Excerpt da transcript

I am Gerald Combmes. Uh I'm more well known as the creator and lead developer of Wireshark, but I am also a Falco maintainer. And what did I do? I'm sorry. Hold on. Uh first of all, Falco, if you're not familiar with it, it is a cloudnative real-time threat detection engine. Uh typically you would deploy it in a Kubernetes cluster and it will sit there and monitor your system calls and log messages and match them against a set of rules and if any of those rules trigger you get an alert. Um Falco does a great job with this. A lot of people use it and have been for the last 10 years. It's about to celebrate its 10-y year anniversary. But one of the neat things that we added in Falco recently was the ability to take that activity whenever it triggers one of those rules and save it out to a capture file. And the idea behind that is to let you then do more investigative analysis using a tool called Stratark, which is something that I've been working on. Stratosark is a sibling application of Wireshark that lets you do more investigative analysis.

It uses the same user interface as Wireshark. It uses the same dissection engine. So you can take all these workflows that you would normally use in the packet world and apply them to system calls and log messages. And so you know the idea is that we take a really nice workflow that we have on the networking side and we've had for I don't know the past 20 25 years where you have all these tools that are based around lib pcap and its file formats and you know you would kind of move that over and replicate that on the system call side with with falco and stratark and you know the libraries that they use and hopefully more applications will pop over time. Now, last year at CubeCon North America, I gave a demo of using Stratark with Falco and um I I focused mainly on the Stratark side and and I finished up the talk showing that the that you can actually use these tools to look at data that was transmitted across a pipe. Uh in this case, somebody was trying to exploit a uh an SSH key. But I didn't really talk about the Falco side of this and and uh if you'll indulge me, that's what I'd like to do here today.

Uh on the Falco side, you need to make some changes to Falco's configuration file, which is Falco. by by default. Um and Falco's configuration is is documented in the URL you see at the top of the the screen. But to enable capture, you have to go down to the capture section and say enabled true. Um it's it's it's fals
