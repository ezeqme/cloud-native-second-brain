---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2025 - Atlanta, United States"
event_id: kccncna2025
year: 2025
region: "North America"
city: "Atlanta"
country: "United States"
event_date: "2025-11-10/2025-11-13"
track: "Observability"
themes: ["Observability", "Kubernetes Core"]
speakers: ["Cat Morris", "Derik Evangelista", "Syntasso"]
sched_url: https://kccncna2025.sched.com/event/27FZi/from-panic-to-peace-making-k8s-controller-observability-suck-less-cat-morris-derik-evangelista-syntasso
youtube_search_url: https://www.youtube.com/results?search_query=From+Panic+To+Peace%3A+Making+K8s+Controller+Observability+Suck+Less+CNCF+KubeCon+2025
slides: []
status: parsed
---

# From Panic To Peace: Making K8s Controller Observability Suck Less - Cat Morris & Derik Evangelista, Syntasso

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[Observability]]
- Temas: [[Observability]], [[Kubernetes Core]]
- País/cidade: United States / Atlanta
- Speakers: Cat Morris, Derik Evangelista, Syntasso
- Schedule: https://kccncna2025.sched.com/event/27FZi/from-panic-to-peace-making-k8s-controller-observability-suck-less-cat-morris-derik-evangelista-syntasso
- Busca YouTube: https://www.youtube.com/results?search_query=From+Panic+To+Peace%3A+Making+K8s+Controller+Observability+Suck+Less+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre From Panic To Peace: Making K8s Controller Observability Suck Less.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27FZi/from-panic-to-peace-making-k8s-controller-observability-suck-less-cat-morris-derik-evangelista-syntasso
- YouTube search: https://www.youtube.com/results?search_query=From+Panic+To+Peace%3A+Making+K8s+Controller+Observability+Suck+Less+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=1P76Roya9oQ
- YouTube title: From Panic To Peace: Making K8s Controller Observability Suck Less - Cat Morris & Derik Evangelista
- Match score: 0.898
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/from-panic-to-peace-making-k8s-controller-observability-suck-less/1P76Roya9oQ.txt
- Transcript chars: 30914
- Keywords: information, product, logs, little, status, actually, controller, promise, observability, cubectl, happens, resources, making, chapter, experience, another, platform, victor

### Resumo baseado na transcript

Uh, we're here to talk to you a little bit about going from panic to peace and making your Kubernetes controller observability suck a little bit less. And we're going to do this by way of a bit of a by way of a bit of a story. He realized he might not actually be solving the problems that he needed to solve in finding the princess. And today we're going to talk about from panic to peace making Kubernetes controllers of stability success which will include some lessons that we learned when building kics because kics day is a kubernetes controller and we learn a lot building it. And one of my favorite parts of being a product manager is I get the inside scoop of customers problems. It was a community of practice event with one of our key customers and they were demoing our product and in particular how they debug using it.

### Excerpt da transcript

So, hi everybody. Uh, we're here to talk to you a little bit about going from panic to peace and making your Kubernetes controller observability suck a little bit less. And we're going to do this by way of a bit of a by way of a bit of a story. So, we've got four chapters in this story for you today. We've got starting with a fairy tale of finding and fixing a problem. We're going to go on Sid's epic debugging journey in chapter 2. Uh then we're going to see Victor's grand Kubernetes expectations and finally finish off with the observability onion. So chapter one, the fairy tale of finding and fixing a problem. So once upon a time there was an ogre named Shrek. And Shrek lived happily alone in his swamp until one day that began like any other Shrek heard a noise. What could that be? He wondered. He left his dinner to investigate and found someone in his house. No problem, he thought. He grabbed the intruder and threw them out. But when he stepped outside, there was absolute chaos. There was panic. His worst fears had come true.

Fairy tale creatures were everywhere, ruining his peace. His home was overrun. And his old scary yoga routine wasn't working. Whatever had happened, fixing the problem would take more than just roaring at it. So Shrek traveled to the city to ask Lord Farquad for help. And after many misunderstandings and pointless battles, uh, he learned that to reclaim his swamp, he must rescue a princess from a distant tower. He journeyed through perilous lands, dodged dangers, and even survived a dragon, who surprisingly wasn't as fearsome as she looked. Burned, bruised, but still determined, he rescued the princess. On the way home, Shrek began to wonder if returning her to Farquad wasn't the right thing to do. Maybe there was a better solution to his problems. But when he overheard a conversation that seemed to confirm his worst fears, he abandoned that hope and went back to the original plan. After handing the princess over, Shrek realized he'd made a terrible mistake. And so, with the help of his loyal friends, he fought back and rescued her once more and brought her home.

And together, they all lived happily ever after. So, what's the moral of Shrek? The moral of our story here, uh, firstly, Shrek found that things were good in his swamp until they weren't. He realized he might not actually be solving the problems that he needed to solve in finding the princess. And he went on so many misdirection and false starts that he found out that kn
