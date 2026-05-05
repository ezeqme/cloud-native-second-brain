---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2023 - Chicago, United States"
event_id: kccncna2023
year: 2023
region: "North America"
city: "Chicago"
country: "United States"
event_date: "2023-11-06/2023-11-09"
track: "Observability"
themes: ["Observability"]
speakers: ["Eduardo Silva", "Calyptia"]
sched_url: https://kccncna2023.sched.com/event/1R2s9/logging-deep-dive-and-best-practices-eduardo-silva-calyptia
youtube_search_url: https://www.youtube.com/results?search_query=Logging+Deep+Dive+and+Best+Practices+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Logging Deep Dive and Best Practices - Eduardo Silva, Calyptia

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2023 - Chicago, United States
- Trilha oficial: [[Observability]]
- Temas: [[Observability]]
- País/cidade: United States / Chicago
- Speakers: Eduardo Silva, Calyptia
- Schedule: https://kccncna2023.sched.com/event/1R2s9/logging-deep-dive-and-best-practices-eduardo-silva-calyptia
- Busca YouTube: https://www.youtube.com/results?search_query=Logging+Deep+Dive+and+Best+Practices+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Logging Deep Dive and Best Practices.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2023.sched.com/event/1R2s9/logging-deep-dive-and-best-practices-eduardo-silva-calyptia
- YouTube search: https://www.youtube.com/results?search_query=Logging+Deep+Dive+and+Best+Practices+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=1dQd2seQrkA
- YouTube title: Logging Deep Dive and Best Practices - Eduardo Silva, Calyptia
- Match score: 0.838
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/logging-deep-dive-and-best-practices/1dQd2seQrkA.txt
- Transcript chars: 28864
- Keywords: information, fluent, logs, memory, output, pressure, metrics, endpoint, sending, sometimes, everybody, everything, collect, practices, messages, running, processing, chunks

### Resumo baseado na transcript

welcome everybody to the session about a loging and best practices we're really happy to be here in cucon and I don't know how many times we have been here but really happy to sharing what's new and how you can deal with escalab ility problems today we were going to try to do a more Hands-On session more than just going through a slides so I know we're going to get a lot of Q&A we will try to fit all the Q&A during the session but if we

### Excerpt da transcript

welcome everybody to the session about a loging and best practices we're really happy to be here in cucon and I don't know how many times we have been here but really happy to sharing what's new and how you can deal with escalab ility problems today we were going to try to do a more Hands-On session more than just going through a slides so I know we're going to get a lot of Q&A we will try to fit all the Q&A during the session but if we don't have enough time we just go out of the room we can be there for an hour talking about best practic issues or everything that you need to solve so feel free to just raise your hand uh at the end of the talk or just talk to us at the end and as I said we got access to an uh the early version of the fluent bit book for kubernetes so just scan the QR code fill up the form if you want to get access to it so we will start talking about the challenges that we gotten login and the main purpose of login is not to do login or stct data actually is just do data analysis but if you want to do data analysis you need to extract the information for that gives you the relevant insight for what's going on in applications or services and with this I'm talking from the kernel to user space applications containers and everything that you have in the middle and when you got an issue and you want to travel shoot things yeah everybody ask hey we are the logs give us the logs but sometimes having more logs doesn't give you more value right actually more Telemetry data sometimes can add a lot of noise which makes it really hard to get extract the insights from your environment Services write login information to different places and usually in different formats for example engx has the access log well you can configure that for different type of VOR host in different type of path while other applications prefer to use the CIS looc system where those CIS looc messages might end it up in a different location but as you can see the content is quite different and if you're a lovely user of Windows you might end it up with the events in a different place that can be only accessed by through some weird API through the system and I say weird because it's really complex to do it okay and login is doesn't we don't talk about just the file system log information can exist anywhere and it could be yeah barlock messages barlock containers but also if you want to read the login information from the kernel you want to open the the kernel the kernel message
