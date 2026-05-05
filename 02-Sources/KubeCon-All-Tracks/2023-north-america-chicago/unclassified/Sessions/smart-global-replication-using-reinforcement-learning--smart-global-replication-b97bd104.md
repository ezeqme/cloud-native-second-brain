---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2023 - Chicago, United States"
event_id: kccncna2023
year: 2023
region: "North America"
city: "Chicago"
country: "United States"
event_date: "2023-11-06/2023-11-09"
track: "Unclassified"
themes: ["Cloud Native"]
speakers: ["Benjamin Bengfort", "Rotational Labs"]
sched_url: https://kccncna2023.sched.com/event/1R2mu/smart-global-replication-using-reinforcement-learning-benjamin-bengfort-rotational-labs
youtube_search_url: https://www.youtube.com/results?search_query=Smart+Global+Replication+Using+Reinforcement+Learning+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Smart Global Replication Using Reinforcement Learning - Benjamin Bengfort, Rotational Labs

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2023 - Chicago, United States
- Trilha oficial: [[Unclassified]]
- Temas: [[Cloud Native]]
- País/cidade: United States / Chicago
- Speakers: Benjamin Bengfort, Rotational Labs
- Schedule: https://kccncna2023.sched.com/event/1R2mu/smart-global-replication-using-reinforcement-learning-benjamin-bengfort-rotational-labs
- Busca YouTube: https://www.youtube.com/results?search_query=Smart+Global+Replication+Using+Reinforcement+Learning+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Smart Global Replication Using Reinforcement Learning.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2023.sched.com/event/1R2mu/smart-global-replication-using-reinforcement-learning-benjamin-bengfort-rotational-labs
- YouTube search: https://www.youtube.com/results?search_query=Smart+Global+Replication+Using+Reinforcement+Learning+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=YTF2dXNhFzI
- YouTube title: Smart Global Replication Using Reinforcement Learning - Benjamin Bengfort, Rotational Labs
- Match score: 0.837
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/smart-global-replication-using-reinforcement-learning/YTF2dXNhFzI.txt
- Transcript chars: 34435
- Keywords: learning, reinforcement, actually, systems, consistency, probability, distributed, rights, epsilon, called, question, replica, visibility, latency, reward, policies, function, rewards

### Resumo baseado na transcript

I think it's time for me to get started hello everyone and uh thank you for joining me for my talk uh today I'd like to tell the story of a distributed data system that we built for one of our clients that's globally distributed and that we optimized using reinforcement learning uh to save a bunch of money uh so hopefully it'll be an entertaining story um first though I should talk about the motivating use case and give you a little bit of background of of why we

### Excerpt da transcript

I think it's time for me to get started hello everyone and uh thank you for joining me for my talk uh today I'd like to tell the story of a distributed data system that we built for one of our clients that's globally distributed and that we optimized using reinforcement learning uh to save a bunch of money uh so hopefully it'll be an entertaining story um first though I should talk about the motivating use case and give you a little bit of background of of why we were building this thing uh in 2016 FFF the financial action task force in the United States uh wrote a rule that said cryptocurrencies and blockchain virtual assets like nfts now have to be regulated like Banks so that when assets of a certain Fiat value cross a border that they are under the regulation of What's called the travel Rule and with the travel rule means is that vasp virtual asset service providers which are kind of like blockchain Banks they have to perform sanctions checks and know who the originator and who the beneficiary is of any transaction and the purpose of this regulation is anti-money laundering and anti-terrorism and even though that ruling comes from you know a United States regulatory body almost every country in the world has a similar version of this regulation um and so whenever you have now uh in 2023 whenever you have a crossborder blockchain transaction if it's you know Bitcoin or whatever uh you your vasp as long as you're not a self-hosted wallet you must comply with this travel Rule now as you might imagine vasp are tech companies they're interested in consensus and blockchain and and cryptocurrencies and they're not Banks and they don't have big compliance departments as you guys might expect from you know recent news with uh different types of vasp so they got together and they formed a nonprofit open-source working group called trissa so trissa stands for the travel rule information sharing architecture and the goal of trissa was to enable a non-centralized peer-to-peer exchange of the pii information of the account holders in these transactions in order to comply with a travel Rule and as you might expect it was very Tech Centric so they took a certificate Authority model uh they used mtls they wanted it to be decentralized and so it had to be a peer-to-peer sharing Network so that's that's the premise of this application so what does trissa do well in a peer-to-peer Network you have to figure out who your peers are right and you have to be able to trust you
