---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Solutions Showcase"
themes: ["Storage Data", "Kubernetes Core"]
speakers: ["Gabriele Bartolini", "EDB and Laurent Parodi", "HSBC"]
sched_url: https://kccnceu2026.sched.com/event/2EG01/cloud-native-theater-data-on-kubernetes-day-from-vms-to-kubernetes-in-a-large-global-bank-a-dbas-journey-gabriele-bartolini-edb-and-laurent-parodi-hsbc
youtube_search_url: https://www.youtube.com/results?search_query=Cloud+Native+Theater+%7C+Data+on+Kubernetes+Day%3A+From+VMs+to+Kubernetes+in+a+Large+Global+Bank%3A+A+DBA%27s+Journey+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Cloud Native Theater | Data on Kubernetes Day: From VMs to Kubernetes in a Large Global Bank: A DBA's Journey - Gabriele Bartolini, EDB and Laurent Parodi, HSBC

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Solutions Showcase]]
- Temas: [[Storage Data]], [[Kubernetes Core]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Gabriele Bartolini, EDB and Laurent Parodi, HSBC
- Schedule: https://kccnceu2026.sched.com/event/2EG01/cloud-native-theater-data-on-kubernetes-day-from-vms-to-kubernetes-in-a-large-global-bank-a-dbas-journey-gabriele-bartolini-edb-and-laurent-parodi-hsbc
- Busca YouTube: https://www.youtube.com/results?search_query=Cloud+Native+Theater+%7C+Data+on+Kubernetes+Day%3A+From+VMs+to+Kubernetes+in+a+Large+Global+Bank%3A+A+DBA%27s+Journey+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Cloud Native Theater | Data on Kubernetes Day: From VMs to Kubernetes in a Large Global Bank: A DBA's Journey.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2EG01/cloud-native-theater-data-on-kubernetes-day-from-vms-to-kubernetes-in-a-large-global-bank-a-dbas-journey-gabriele-bartolini-edb-and-laurent-parodi-hsbc
- YouTube search: https://www.youtube.com/results?search_query=Cloud+Native+Theater+%7C+Data+on+Kubernetes+Day%3A+From+VMs+to+Kubernetes+in+a+Large+Global+Bank%3A+A+DBA%27s+Journey+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=m0LBKjlxrog
- YouTube title: Cloud Native Theater | Data on Kubernetes Day: From VMs to Ku... Gabriele Bartolini & Laurent Parodi
- Match score: 0.794
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/cloud-native-theater-data-on-kubernetes-day-from-vms-to-kubernetes-in/m0LBKjlxrog.txt
- Transcript chars: 20589
- Keywords: database, posgress, native, platform, patching, failover, security, operator, posgus, replication, recovery, foundation, control, directly, global, finally, databases, extensions

### Resumo baseado na transcript

They led the charge to co-design the internal datab database platform uh for the bank. My name is Gabriel and today with Lauran we will talk about the journey that his organization has taken with posgress kubernetes and cloud nativep. So we will divide the presentation in five parts where we'll so we'll start where we came from the VMs and then walk through the new blueprint we designed how we modernize the stack why cloud native PG became the engine of the stack and finally where we headed. The data must stay on our own systems and we have strict cyber security controls, auditing, patching, SLAs, secrets management and the list goes on. One to kill the technical depth and a strategic imperative to reduce the total cost of ownership of the database platform. We were moving from legacy custom monitoring to native promises metrics with deep fleetwide visibility.

### Excerpt da transcript

So they said that the DBA role was dying in the cloud native era. They were wrong. At HSBC, the DBA didn't just survive the move to Kubernetes. They led the charge to co-design the internal datab database platform uh for the bank. So welcome to data on Kubernetes. My name is Gabriel and today with Lauran we will talk about the journey that his organization has taken with posgress kubernetes and cloud nativep. So I'm uh Gabriela I'm a data on kubernetes uh am community ambassador so I'm I'm really happy to be here today at this event and uh I'm also a posgus contributor. I've been using posgus for 25 years and uh I'm also uh a cloud native PG maintainer since you know six years ago I started to with my team here uh to bring uh the database uh to kubernetes and I work for EDB I'm a VP chief architect uh for Kubernetes >> thank you and I am Lauren Parody I work for HSBC I'm the global product owner for posgress SQL So before we dive into the future of the cloud, I wanted to take a moment uh to look back.

Tomorrow marks exactly two years since the posgus community lost prematurely one of its brightest lights, Simon Riggs. Simon was a visionary and the primary architect behind many of the features that moved posgress from a standalone database to the enterprisegrade solutions that it is today. Over two decades, his vision and his code helped shape the database that we all know and love. But beyond the technology, Simon was a friend, a mentor, and a leader. So the QR code that you see here points to his last p public speech uh titled the next the next 20 years for posgress in which he laid out the vision for where posgress needs to go next. So thank you Simon. >> Thank you Gabriel. So we will divide the presentation in five parts where we'll so we'll start where we came from the VMs and then walk through the new blueprint we designed how we modernize the stack why cloud native PG became the engine of the stack and finally where we headed. So it's like this windmill. It was solid, built to last, but it was designed for a different era.

That was our VM world. HSBC is one of the world's largest banks operating in 56 countries with 40 millions of clients and thousands of IT engineers. We have been managing posgress SQL for long time and crafted a robust and realable database infrastructure using VMs. We built complex tooling with shell scripts, open source solutions backed by unseable playbooks and API to hide the complexity of the regular DBA tasks from the users
