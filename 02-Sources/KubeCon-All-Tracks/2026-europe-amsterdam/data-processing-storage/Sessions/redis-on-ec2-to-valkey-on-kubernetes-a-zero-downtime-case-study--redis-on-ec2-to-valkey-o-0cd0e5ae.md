---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Data Processing + Storage"
themes: ["Storage Data", "Kubernetes Core"]
speakers: ["Joe Heyburn", "Braze"]
sched_url: https://kccnceu2026.sched.com/event/2CW6D/redis-on-ec2-to-valkey-on-kubernetes-a-zero-downtime-case-study-joe-heyburn-braze
youtube_search_url: https://www.youtube.com/results?search_query=Redis+on+EC2+to+Valkey+on+Kubernetes%3A+A+Zero-Downtime+Case+Study+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Redis on EC2 to Valkey on Kubernetes: A Zero-Downtime Case Study - Joe Heyburn, Braze

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Data Processing + Storage]]
- Temas: [[Storage Data]], [[Kubernetes Core]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Joe Heyburn, Braze
- Schedule: https://kccnceu2026.sched.com/event/2CW6D/redis-on-ec2-to-valkey-on-kubernetes-a-zero-downtime-case-study-joe-heyburn-braze
- Busca YouTube: https://www.youtube.com/results?search_query=Redis+on+EC2+to+Valkey+on+Kubernetes%3A+A+Zero-Downtime+Case+Study+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Redis on EC2 to Valkey on Kubernetes: A Zero-Downtime Case Study.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2CW6D/redis-on-ec2-to-valkey-on-kubernetes-a-zero-downtime-case-study-joe-heyburn-braze
- YouTube search: https://www.youtube.com/results?search_query=Redis+on+EC2+to+Valkey+on+Kubernetes%3A+A+Zero-Downtime+Case+Study+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=rNZ6HLiFgYI
- YouTube title: Redis on EC2 to Valkey on Kubernetes: A Zero-Downtime Case Study - Joe Heyburn, Braze
- Match score: 0.955
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/redis-on-ec2-to-valkey-on-kubernetes-a-zero-downtime-case-study/rNZ6HLiFgYI.txt
- Transcript chars: 22558
- Keywords: cluster, sentinel, valkey, migration, primary, running, change, itself, downtime, across, server, without, message, container, customer, number, replicas, pretty

### Resumo baseado na transcript

My name's Joe Hayburn and I work at Braze as a staff engineer on the in-memory database team. And in 2022, we decided to see just how crazy we could be by migrating nearly 300 Redis instances to Kubernetes. Just to give you a bit of an idea on the scale that we're running at here at Braze, just this month, we have about 600 highly available instances, which we call shards. And each type has can have one or more shards to allow allow it to individually horizontally scale out. Now, we already had a greenfield cluster that was running on Kubernetes, and we had deployed Redis to that with a Helm chart. Which when you mix that in in a Kubernetes world, you're then going to have the pod IP change if that pod were to roll.

### Excerpt da transcript

Let me actually get started and introduce myself. My name's Joe Hayburn and I work at Braze as a staff engineer on the in-memory database team. And in 2022, we decided to see just how crazy we could be by migrating nearly 300 Redis instances to Kubernetes. And we did all of that without any downtime and a rollback path at every step of the way. But more importantly than that, I want to show you all here today what that migration to Kubernetes allowed us to achieve, which was a completely seamless migration to Valkey, which helped us along the way to unlock a latency improvement of up to 90%. For those who don't know Braze, we are a customer engagement platform. We help brands to send the right message to the right person at the right time. And when I talk about messages, I'm talking about highly personalized real-time engagements that can be sent over a number of channels. Like, I think we support emails, push notifications, SMS, and I think we even have some customers that hook into letters, physical letters.

Are they still a thing? This customer is using them. The messages can be sent as a result of the data that we ingest via our APIs. So here you can see how the typical message flow works here. And this helps to enable campaigns such as a welcome email to a new customer on signup or scheduling a message to a customer that might have abandoned their basket. And that message could be a push notification with a coupon to engage them back onto the platform. Even we can even cancel those scheduled messages if the customer comes back and completes that purchase without before that message has even been sent. And we're doing all of that billions of times every single day. Braze has over 2,000 customers that expect us to scale with them. So we have got to make sure that Valkey can scale with them, too. When I talk about Valkey at Braze, though, I'm not just talking about one workload. I'm talking we use it for a number of different things, right? We use it for rate limiting, distributed locks, message deduplication, and as well as that, Sidekiq.

And if you know Sidekiq, then you know that Valkey is at the very heart of it, right? So when I talk about Valkey at Braze here, I'm talking about the entire backbone of the Braze platform. Just to give you a bit of an idea on the scale that we're running at here at Braze, just this month, we have about 600 highly available instances, which we call shards. And between all of them, they process over 36 million operati
