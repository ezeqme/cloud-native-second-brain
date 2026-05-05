---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States"
event_id: kccncna2024
year: 2024
region: "North America"
city: "Salt Lake City"
country: "United States"
event_date: "2024-11-12/2024-11-15"
track: "Operations + Performance"
themes: ["SRE Reliability"]
speakers: ["Trey Caliva", "Global Payments"]
sched_url: https://kccncna2024.sched.com/event/1i7ll/setting-new-standards-for-reliability-in-cloud-native-multi-region-applications-trey-caliva-global-payments
youtube_search_url: https://www.youtube.com/results?search_query=Setting+New+Standards+for+Reliability+in+Cloud+Native+Multi-Region+Applications+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Setting New Standards for Reliability in Cloud Native Multi-Region Applications - Trey Caliva, Global Payments

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[Operations + Performance]]
- Temas: [[SRE Reliability]]
- País/cidade: United States / Salt Lake City
- Speakers: Trey Caliva, Global Payments
- Schedule: https://kccncna2024.sched.com/event/1i7ll/setting-new-standards-for-reliability-in-cloud-native-multi-region-applications-trey-caliva-global-payments
- Busca YouTube: https://www.youtube.com/results?search_query=Setting+New+Standards+for+Reliability+in+Cloud+Native+Multi-Region+Applications+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Setting New Standards for Reliability in Cloud Native Multi-Region Applications.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1i7ll/setting-new-standards-for-reliability-in-cloud-native-multi-region-applications-trey-caliva-global-payments
- YouTube search: https://www.youtube.com/results?search_query=Setting+New+Standards+for+Reliability+in+Cloud+Native+Multi-Region+Applications+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=rLxsIEy20So
- YouTube title: Setting New Standards for Reliability in Cloud Native Multi-Region Applications - Trey Caliva
- Match score: 1.009
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/setting-new-standards-for-reliability-in-cloud-native-multi-region-app/rLxsIEy20So.txt
- Transcript chars: 37483
- Keywords: cockroach, regions, global, little, region, cluster, obviously, write, payment, database, application, active, question, legacy, traffic, native, payments, whether

### Resumo baseado na transcript

i' like to introduce myself I'm Trey CA a principal Cloud architect at Global Payments and I'm Jim Hatcher I'm a Solutions architect at cockroach Labs thanks and we're going to be talking today about setting new standards for reliability and Cloud native applications so kind of first let's set the stage of kind of a little bit what we do and why we do it um so reliable payment processing is obviously fundamental to the global economy so how many people today use their credit card or use their

### Excerpt da transcript

i' like to introduce myself I'm Trey CA a principal Cloud architect at Global Payments and I'm Jim Hatcher I'm a Solutions architect at cockroach Labs thanks and we're going to be talking today about setting new standards for reliability and Cloud native applications so kind of first let's set the stage of kind of a little bit what we do and why we do it um so reliable payment processing is obviously fundamental to the global economy so how many people today use their credit card or use their phone to tap something you know or you know yeah so pretty much everybody right um so whether it's your you know you're tapping swiping dipping the card tap on your phone this happens all day every day and it it really is a fundamental part of the economy today one of the things that that I like to think about is it's very much like a utility um one of those things that when it's not it's great and then you don't really notice it until it's not there and you know when we look at this it's it's it's very much that important right if we have a huge outage um it can affect not just our clients not just us it can actually affect the entire economy so who are we so Global Payments we have about 5 million Merchant accounts um have about 38 countries where where we have a physical presence um and we do about 75 billion transactions annually um about 27,000 employees worldwide we're based out of Atlanta um but we obviously have offices all over the world um Fortune 500 company so never heard of us that's okay um but I guarantee you if you've used your credit card in the past last you know week you we've probably touched your touched your payment information so our unique challenges um kind of want to get into a little bit of what what is goes into a payment authorization because it helps to understand what our what our challenges are so if you're a customer right you go to a merchant whether it's Starbucks whether it's you know e-commerce um you're going to you're going to pay them you're going to tap your card you're going to click a link that's going to go to what we call a payment Gateway that payment Gateway is going to H handle the routing and the authorization of that transaction um that authorization is going to hit um an issuing bank it's going to hit a card brand like Visa or Mastercard um and those things are you know all have to happen very quickly so when we look at the payment Gateway itself is the primary application we're going to talk about today we've got to
