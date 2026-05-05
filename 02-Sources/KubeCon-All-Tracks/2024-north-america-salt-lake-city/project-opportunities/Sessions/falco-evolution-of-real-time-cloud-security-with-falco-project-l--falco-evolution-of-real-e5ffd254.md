---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States"
event_id: kccncna2024
year: 2024
region: "North America"
city: "Salt Lake City"
country: "United States"
event_date: "2024-11-12/2024-11-15"
track: "Project Opportunities"
themes: ["Security"]
speakers: []
sched_url: https://kccncna2024.sched.com/event/1iWA0/falco-evolution-of-real-time-cloud-security-with-falco-project-lightning-talk
youtube_search_url: https://www.youtube.com/results?search_query=Falco%3A+Evolution+of+Real+Time+Cloud+Security+with+Falco+%7C+Project+Lightning+Talk+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Falco: Evolution of Real Time Cloud Security with Falco | Project Lightning Talk

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[Project Opportunities]]
- Temas: [[Security]]
- País/cidade: United States / Salt Lake City
- Speakers: N/A
- Schedule: https://kccncna2024.sched.com/event/1iWA0/falco-evolution-of-real-time-cloud-security-with-falco-project-lightning-talk
- Busca YouTube: https://www.youtube.com/results?search_query=Falco%3A+Evolution+of+Real+Time+Cloud+Security+with+Falco+%7C+Project+Lightning+Talk+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Falco: Evolution of Real Time Cloud Security with Falco | Project Lightning Talk.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1iWA0/falco-evolution-of-real-time-cloud-security-with-falco-project-lightning-talk
- YouTube search: https://www.youtube.com/results?search_query=Falco%3A+Evolution+of+Real+Time+Cloud+Security+with+Falco+%7C+Project+Lightning+Talk+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=e2wO3lxzjEA
- YouTube title: Falco: Evolution of Real Time Cloud Security with Falco | Project Lightning Talk
- Match score: 1.08
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/falco-evolution-of-real-time-cloud-security-with-falco-project-lightni/e2wO3lxzjEA.txt
- Transcript chars: 4399
- Keywords: events, evolution, security, maintainers, excited, actually, simple, language, happens, whatever, monitor, course, created, detection, containers, infrastructure, process, interested

### Resumo baseado na transcript

hey everyone thank you for joining me uh talking today about Falco so I'm Luca and I'm one of the maintainers for the Falco project I work at csig the company that originally created Falco so today I would like to uh tell you a bit about the evolution of the project what it does and what we're excited about so if you don't know what Falco is uh Falco is a graduated project from the cncf and you could read on the website that Falco is an open source

### Excerpt da transcript

hey everyone thank you for joining me uh talking today about Falco so I'm Luca and I'm one of the maintainers for the Falco project I work at csig the company that originally created Falco so today I would like to uh tell you a bit about the evolution of the project what it does and what we're excited about so if you don't know what Falco is uh Falco is a graduated project from the cncf and you could read on the website that Falco is an open source runtime security solution for thre detection cross kubernetes containers host and the cloud but what does that actually mean and how uh we got to where Falco is today so generally speaking Falon monitors your infrastructure for security events so whether it's a host kubernetes or containers uh we've got monitoring and this has been true since day one so how do we do it it's the core the essence of Falon is the fact that we have a very simple and easy to understand language for specifying rules in this in this case we want to be alerted every time a process opens a specific file that we are interested in that's very simple and core to Falon and in fact every time this happens you will get an alert in the form of a message so this was great and how we do that under the hood is really not important as long as this action work this was great but people started asking so what do I do with my events I I have them so what can I do and so FAL evolved to have a lot of channels that you can use to Output your events so we have a lot of things that you can actually build yourself if you want and we have a new uh it was new back then a project called Falco sidekick that has more than 60 Integrations to slack to your cm to elastic databases cues whatever you can think of there is an integration for it and uh uh later during the evolution of the project we thought that CIS calls are cool because these events opening a file creating a process and these kind of things are system calls in the kernel but what else can we monitor we have kubernetes and kubernetes has audit events for example but we also run things in our infrastructure from cloud providers and Cloud providers have their own audit log so how do we do it how do we get Falco to monitor those as well we have created a plugin system for a couple years now that has uh right right now you can find more than 20 plugins and you can pretty much monitor whatever you want you can find uh you can find the AWS cloud trail uh octal logs gcp kubernetes audit events and many more
