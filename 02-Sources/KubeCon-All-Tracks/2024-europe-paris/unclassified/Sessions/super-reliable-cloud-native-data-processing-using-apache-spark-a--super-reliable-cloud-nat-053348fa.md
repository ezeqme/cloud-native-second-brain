---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2024 - Paris, France"
event_id: kccnceu2024
year: 2024
region: "Europe"
city: "Paris"
country: "France"
event_date: "2024-03-19/2024-03-22"
track: "Unclassified"
themes: ["AI ML", "Storage Data"]
speakers: ["Bo Yang", "HAI TAO", "Apple"]
sched_url: https://kccnceu2024.sched.com/event/1YeNG/super-reliable-cloud-native-data-processing-using-apache-spark-and-cloud-shuffle-manager-bo-yang-hai-tao-apple
youtube_search_url: https://www.youtube.com/results?search_query=Super+Reliable+Cloud+Native+Data+Processing+Using+Apache+Spark+and+Cloud+Shuffle+Manager+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Super Reliable Cloud Native Data Processing Using Apache Spark and Cloud Shuffle Manager - Bo Yang & HAI TAO, Apple

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[Unclassified]]
- Temas: [[AI ML]], [[Storage Data]]
- País/cidade: France / Paris
- Speakers: Bo Yang, HAI TAO, Apple
- Schedule: https://kccnceu2024.sched.com/event/1YeNG/super-reliable-cloud-native-data-processing-using-apache-spark-and-cloud-shuffle-manager-bo-yang-hai-tao-apple
- Busca YouTube: https://www.youtube.com/results?search_query=Super+Reliable+Cloud+Native+Data+Processing+Using+Apache+Spark+and+Cloud+Shuffle+Manager+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Super Reliable Cloud Native Data Processing Using Apache Spark and Cloud Shuffle Manager.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1YeNG/super-reliable-cloud-native-data-processing-using-apache-spark-and-cloud-shuffle-manager-bo-yang-hai-tao-apple
- YouTube search: https://www.youtube.com/results?search_query=Super+Reliable+Cloud+Native+Data+Processing+Using+Apache+Spark+and+Cloud+Shuffle+Manager+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=tWClCHUd2lA
- YouTube title: Super Reliable Cloud Native Data Processing Using Apache Spark and Cloud Shuffle Manager
- Match score: 1.08
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/super-reliable-cloud-native-data-processing-using-apache-spark-and-clo/tWClCHUd2lA.txt
- Transcript chars: 21724
- Keywords: storage, shuffle, executor, manager, another, enable, dynamic, basically, solution, previous, allocation, simple, application, trying, question, cost, running, multiple

### Resumo baseado na transcript

hi everyone yeah thank you for coming this session okay yeah my name is B so I'm coming from Apple and uh I have been working in the Big Data area for about about more than 10 years so it's a long time and now I'm in apple building data platform and the Machine learning platform yeah very nice to see you here so my colleague uh hi Buu my name is hi I also from Apple and I work in the data infer team uh so I'm glad to

### Excerpt da transcript

hi everyone yeah thank you for coming this session okay yeah my name is B so I'm coming from Apple and uh I have been working in the Big Data area for about about more than 10 years so it's a long time and now I'm in apple building data platform and the Machine learning platform yeah very nice to see you here so my colleague uh hi Buu my name is hi I also from Apple and I work in the data infer team uh so I'm glad to be here talking about uh uh reliability and cost efficiency uh for running spark uh using Co in the cloud thank you great let's get started so this is talk about CL native data processing and also about aachi spark so I want to do a very quick survey so here how many people use Spark before Oh great okay you are in the right place and I'm in the right place okay nice here is a quick agenda we will maybe very quickly introduce spark and how F tolerance Works in spark then we will present what kind of problem we try to solve let's tell some problem with spark and uh there are already many solutions they are built for different reasons so you will see a lot of and we build another solution uh now we call Cloud Shuffle manager CSM and we will explain how it works what benefit it has then hopefully you we can have more discussion so please uh if you have any questions so we can discuss more yeah yeah very quick about Spar spark was created about uh 15 years ago it's a long time and it is unified framework to do dat processing a very large scale it's very fast how it works it it is underline it's map reduce very simple concept brought by Google if you have very large amount of data it splits data in small chunks and process those chunks in parallel so you can use your computer power to Pro that them in massively scale and run it very quickly and original was running in your own data center like a yarn and these days people bring spark to Cloud error it can run on community cool yeah very small kind of explaining about how map reduce Works uh map reduce proves a data in two stage the first stage is map it split data and put Rel dated data together on each machine here we call executor here is a SQL statement select word and count to do a word counting very simple uh SQL execution so the map side get a data split then it will Shuffle the data and get the same word to the same place then in the reducer side it just count each word and generate the output file which count how many words appeared underline spark is just very simple like this even though
