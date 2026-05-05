---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2025 - Atlanta, United States"
event_id: kccncna2025
year: 2025
region: "North America"
city: "Atlanta"
country: "United States"
event_date: "2025-11-10/2025-11-13"
track: "Keynote Sessions"
themes: ["AI ML", "SRE Reliability"]
speakers: ["Artur Souza", "Principal Engineer", "Amazon", "Chunpeng Wang", "Senior Applied Scientist", "Amazon"]
sched_url: https://kccncna2025.sched.com/event/27Fcl/keynote-predictive-scaling-and-capacity-planning-with-machine-learning-at-amazoncom-artur-souza-principal-engineer-amazon-chunpeng-wang-senior-applied-scientist-amazon
youtube_search_url: https://www.youtube.com/results?search_query=Keynote%3A+Predictive+Scaling+and+Capacity+Planning+With+Machine+Learning+at+Amazon.com+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Keynote: Predictive Scaling and Capacity Planning With Machine Learning at Amazon.com - Artur Souza, Principal Engineer, Amazon & Chunpeng Wang, Senior Applied Scientist, Amazon

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[Keynote Sessions]]
- Temas: [[AI ML]], [[SRE Reliability]]
- País/cidade: United States / Atlanta
- Speakers: Artur Souza, Principal Engineer, Amazon, Chunpeng Wang, Senior Applied Scientist, Amazon
- Schedule: https://kccncna2025.sched.com/event/27Fcl/keynote-predictive-scaling-and-capacity-planning-with-machine-learning-at-amazoncom-artur-souza-principal-engineer-amazon-chunpeng-wang-senior-applied-scientist-amazon
- Busca YouTube: https://www.youtube.com/results?search_query=Keynote%3A+Predictive+Scaling+and+Capacity+Planning+With+Machine+Learning+at+Amazon.com+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Keynote: Predictive Scaling and Capacity Planning With Machine Learning at Amazon.com.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27Fcl/keynote-predictive-scaling-and-capacity-planning-with-machine-learning-at-amazoncom-artur-souza-principal-engineer-amazon-chunpeng-wang-senior-applied-scientist-amazon
- YouTube search: https://www.youtube.com/results?search_query=Keynote%3A+Predictive+Scaling+and+Capacity+Planning+With+Machine+Learning+at+Amazon.com+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=C7cKYRg7YwQ
- YouTube title: Keynote: Predictive Scaling and Capacity Planning With Machine Learni... Artur Souza & Chunpeng Wang
- Match score: 0.9
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/keynote-predictive-scaling-and-capacity-planning-with-machine-learning/C7cKYRg7YwQ.txt
- Transcript chars: 13308
- Keywords: scaling, traffic, capacity, forecast, shopping, events, reactive, understand, breaking, friday, imagine, business, course, amazon, cost, amazon.com, impact, enough

### Resumo baseado na transcript

That's a question that we have to answer every year Amazon.com as you can imagine um ahead of the holiday season. There are other holidays, sport events, u sale events, and any kind of external factor that can impact the shopping behavior. Even if you for some reason can scale that fast, are you sure all the capacity is available for you in your cloud provider? Don't get me wrong, reactive scale is cheaper and we want to rely on reactive scaling when possible, but during those events, we need to model ahead. If you have some kind of caching that you have to load ahead of time only after all this is done your service is ready to take load and that's the magic that we take to understand how fast we can scale and descale each service at amazon.com. MTT like I said it tells us how fast your service can scale scale this scale.

### Excerpt da transcript

Hello, CubeCon. I'm Arthur Souza. >> Uh, this is Chong. >> Are we have are we ready to handle Black Friday traffic? That's a question that we have to answer every year Amazon.com as you can imagine um ahead of the holiday season. And it's not only Black Friday, as you can imagine. There are other holidays, sport events, u sale events, and any kind of external factor that can impact the shopping behavior. You might imagine, well, I just going to set up reactive scaling. I'm good to go. Not really. So, we do use reactive scaling, but for those peak events, it's not enough. And practice scaling is needed. And um me and and Champang, we're going to walk you through how u we do this at amazon.com. Um so let's begin with the user journey. Different services are activated by different business demands. For example, when you're looking for a product, you're of course going to activate search and the product detail page services. When you add an item to the shopping cart, it will trigger the shopping cart and other checkout related services.

Once payment is processed, it takes care of the payment through the payment providers, activate those services, and same thing happens for shipping and delivery. It's important to understand the cascade effect of each one of those actions. As you can see, those those activate different services at different magnitudes. A call to one service can result in calls to three different services or four or a multitude of calls to the same service. This complexity also shows why Rex scanning is difficult to work in these scenarios because even if one service can react fast enough, it takes a while to the cascade effect takes care of the entire network of services. Let me go through. Let's understand peak traffic a little bit. In this hypothetical example, we have uh Black Friday and Cyber Mondays. And again, this is a hypothetical example. There is a spike at the beginning. Maybe you just finish uh your Thanksgiving dinner. Hopefully, brush your teeth before you go shopping. But then everybody goes shopping at the beginning.

Then people go to sleep. and then throughout the day more shop activity happens. We can use this example to explain the user journey throughout the day. It also shows that we must understand the shape of the curve, the rate of change and the sustained duration of the peak hours. It's not just understanding the whole load, the entire uh load. Let me walk let look at this again. Look at how steep that initial spike
