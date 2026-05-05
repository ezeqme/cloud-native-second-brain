---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2025 - Atlanta, United States"
event_id: kccncna2025
year: 2025
region: "North America"
city: "Atlanta"
country: "United States"
event_date: "2025-11-10/2025-11-13"
track: "Maintainer Track"
themes: ["AI ML", "SRE Reliability", "Community Governance"]
speakers: ["Leonardo Grasso", "Leonardo Di Giovanna", "Sysdig"]
sched_url: https://kccncna2025.sched.com/event/27No0/beyond-the-clouds-falcos-ascent-in-performance-and-deep-visibility-leonardo-grasso-leonardo-di-giovanna-sysdig
youtube_search_url: https://www.youtube.com/results?search_query=Beyond+the+Cloud%28s%29%3A+Falco%E2%80%99s+Ascent+in+Performance+and+Deep+Visibility+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Beyond the Cloud(s): Falco’s Ascent in Performance and Deep Visibility - Leonardo Grasso & Leonardo Di Giovanna, Sysdig

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[SRE Reliability]], [[Community Governance]]
- País/cidade: United States / Atlanta
- Speakers: Leonardo Grasso, Leonardo Di Giovanna, Sysdig
- Schedule: https://kccncna2025.sched.com/event/27No0/beyond-the-clouds-falcos-ascent-in-performance-and-deep-visibility-leonardo-grasso-leonardo-di-giovanna-sysdig
- Busca YouTube: https://www.youtube.com/results?search_query=Beyond+the+Cloud%28s%29%3A+Falco%E2%80%99s+Ascent+in+Performance+and+Deep+Visibility+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Beyond the Cloud(s): Falco’s Ascent in Performance and Deep Visibility.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27No0/beyond-the-clouds-falcos-ascent-in-performance-and-deep-visibility-leonardo-grasso-leonardo-di-giovanna-sysdig
- YouTube search: https://www.youtube.com/results?search_query=Beyond+the+Cloud%28s%29%3A+Falco%E2%80%99s+Ascent+in+Performance+and+Deep+Visibility+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=5JoNk7_Sors
- YouTube title: Beyond the Cloud(s): Falco’s Ascent in Performance and... Leonardo Grasso & Leonardo Di Giovanna
- Match score: 0.803
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/beyond-the-cloud-s-falcos-ascent-in-performance-and-deep-visibility/5JoNk7_Sors.txt
- Transcript chars: 17584
- Keywords: events, kernel, feature, provide, course, performance, already, information, basically, mechanism, possible, simple, introduced, plug-in, feedback, another, question, snorts

### Resumo baseado na transcript

I'm Lonardo Graaso and here with me there is another Lonardo, Leonardo de Joanna. Uh if you want to reach out to us, please feel free to contact us on GitHub or Slack. [snorts] Then it evaluate do this this event against a set of rules and if any of these rule matches it send an alert. This time I asked clude and surprising um I asked a rule that I used in a demo a lot of time ago and uh it create a similar rules at the first try. Okay, at this point I started enjoying asking question to AI and so I asked to AI to answer to the ultimate question of Falco of security the universe and everything does anybody know the answer the answer is Falco 0.42 42 the latest version [laughter] the latest version Falco that we released in October. And another one that is mostly a huge performance improvement regarding the drop entry initiative that my colleague will speak later.

### Excerpt da transcript

Hey everyone, welcome to the Falcom antenna track. Let's start by presenting ourself. I'm Lonardo Graaso and here with me there is another Lonardo, Leonardo de Joanna. We are both Falcon maintainer. We also uh both work for CDI and we are both Italian. Uh if you want to reach out to us, please feel free to contact us on GitHub or Slack. We can find us on the Falco channel on the compet. So I have been involved in the Falco project since 2020 and uh uh was was uh answered many time this question. what's Falco. So I asked myself what I could say this time. Um but uh you know Falco during the years become very popular and uh I'm I'm a bit lazy lazy person you know as many engineer. So this time I just ask it chat GPT what's falco of course falco of course chat knows very well what falco falco is the opensource and cloudnative security tool uh it was donated to the CNCF it's nowadays a standard for runtime threat detertion it's a graduate project but maybe You can understand more about Falco by looking at how it works and this time asked the Germany of course from an ele point of view it's very simple it capture events from the Linux kernel.

Uh there is also other data source that can be added to Falco by using plugins. I just won't mention this now because during this presentation we will not talk too much about plugins. [snorts] Then it evaluate do this this event against a set of rules and if any of these rule matches it send an alert. It's very very simple. Of course, to achieve this, Falco ships a default set of rules, but uh you can create your own rules, of course, to customize it for your own environment or use case. And since LLM are very good to create code but they are very good also to create falco rules. This time I asked clude and surprising um I asked a rule that I used in a demo a lot of time ago and uh it create a similar rules at the first try. The rules is very simple. just asked uh can you draft a simple falco rule to detect when the webcam of my laptop is being as accessed? And by the way, this is not a mockup. If you uh download the presentation that you can find on SCAD, you will find the link attached to the original uh cloud chat.

Okay, at this point I started enjoying asking question to AI and so I asked to AI to answer to the ultimate question of Falco of security the universe and everything does anybody know the answer the answer is Falco 0.42 42 the latest version [laughter] the latest version Falco that we released in October. S
