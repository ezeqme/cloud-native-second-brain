---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2023 - Chicago, United States"
event_id: kccncna2023
year: 2023
region: "North America"
city: "Chicago"
country: "United States"
event_date: "2023-11-06/2023-11-09"
track: "Emerging + Advanced"
themes: ["Emerging + Advanced"]
speakers: ["David Garcia Valiñas", "Paul Schweigert", "IBM"]
sched_url: https://kccncna2023.sched.com/event/1R2vp/middleware-for-quantum-enabling-advanced-quantum-computing-workflows-david-garcia-valinas-paul-schweigert-ibm
youtube_search_url: https://www.youtube.com/results?search_query=Middleware+for+Quantum%3A+Enabling+Advanced+Quantum+Computing+Workflows+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Middleware for Quantum: Enabling Advanced Quantum Computing Workflows - David Garcia Valiñas & Paul Schweigert, IBM

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2023 - Chicago, United States
- Trilha oficial: [[Emerging + Advanced]]
- Temas: [[Emerging + Advanced]]
- País/cidade: United States / Chicago
- Speakers: David Garcia Valiñas, Paul Schweigert, IBM
- Schedule: https://kccncna2023.sched.com/event/1R2vp/middleware-for-quantum-enabling-advanced-quantum-computing-workflows-david-garcia-valinas-paul-schweigert-ibm
- Busca YouTube: https://www.youtube.com/results?search_query=Middleware+for+Quantum%3A+Enabling+Advanced+Quantum+Computing+Workflows+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Middleware for Quantum: Enabling Advanced Quantum Computing Workflows.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2023.sched.com/event/1R2vp/middleware-for-quantum-enabling-advanced-quantum-computing-workflows-david-garcia-valinas-paul-schweigert-ibm
- YouTube search: https://www.youtube.com/results?search_query=Middleware+for+Quantum%3A+Enabling+Advanced+Quantum+Computing+Workflows+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=XC1jJjBWAXE
- YouTube title: Middleware for Quantum: Enabling Advanced Quantum Computin... David Garcia Valiñas & Paul Schweigert
- Match score: 0.833
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/middleware-for-quantum-enabling-advanced-quantum-computing-workflows/XC1jJjBWAXE.txt
- Transcript chars: 27017
- Keywords: quantum, cluster, classical, cubits, computer, computing, computers, problems, algorithm, circuit, resources, numbers, execution, middleware, pattern, results, running, represent

### Resumo baseado na transcript

y all right thanks for being here at the last session of the day um always nice it's a good turnout for the last session of the day yep hope everybody had a good cubec con um so we're going to talk about middleware for Quantum how we enable uh Advanced Quantum Computing workloads on kubernetes so I'm Paul um I work at IBM I work um in serverless so things like K native um and then also Quantum uh the middleware we're going to talk about today and my

### Excerpt da transcript

y all right thanks for being here at the last session of the day um always nice it's a good turnout for the last session of the day yep hope everybody had a good cubec con um so we're going to talk about middleware for Quantum how we enable uh Advanced Quantum Computing workloads on kubernetes so I'm Paul um I work at IBM I work um in serverless so things like K native um and then also Quantum uh the middleware we're going to talk about today and my colleague yeah I'm David Senor developer in ebm2 developer expert in web Technologies and cloud and yeah that's for me cool all right so we're going to talk about a couple things today um first we're going to just kind of a brief introduction to Quantum Computing what it is why it matters why it's important then we're going to talk about our middleware then we'll run an example application and leave a little bit of time for Q&A at the end Okay so introduction to Quantum um what is quantum Computing and one of the places I always like to start in talking about Quantum is not so much what it is but why it's important and if you remember back to algorithm classes when you looked at you know easy problems and hard problems and we kind of divided algorithms into things that we could do efficiently on classical computers those were our easy problems things that ran in polinomial time and our hard problems things that did you know run exponential time that we couldn't solve In classical computers what Quantum Computing does is it creates a new class of problems something that we call Quantum easy problems but are problems that can be efficiently solved on quantum computers now it's not all NP hard problems but it's some of them so two kind of things to take away from that one is that classical computers aren't going to be replaced by quantum computers um to give an example you know a classical computer can't factor numbers very fast but it can multiply them really fast like you can multiply two numbers on a classical computer in you know milliseconds a quantum computer to multiply two big numbers takes you know a minute or two it's very slow multiplying numbers but factoring them that it can do quickly so again key takeaway point one it's classical and Quantum not replacing classical with Quantum the second is that Ena you know you notice that it's only some problems to be able to use a quantum computer we need to have an efficient Quantum algorithm um an algorithm that can take advantage of how quantum computers work
