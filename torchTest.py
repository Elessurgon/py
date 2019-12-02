import numpy
import torch
import torchvision
import pyro
import tensorflow as tf
import tensorflow_probability as  tfp

loc = 0
scale = 1
normal = torch.distributions.Normal(loc, scale)
x = normal.rsample()

print("sample: {}".format(x))
print("log(sample): {}".format(normal.log_prob(x)))

def weather():
    cloudy = torch.distributions.Bernoulli(0.3).sample()
    condition = "cloudy" if cloudy.item()==1.0 else "sunny"
    mean_temperature = {"cloudy":55.0, "sunny": 75.0}[condition]
    scale_termperature = {"cloudy":10.0, "sunny": 15.0}[condition]
    temp = torch.distributions.Normal(mean_temperature, scale_termperature).rsample()
    return condition, temp.item()

def test():
    weatherCondition, temperature = weather()
    print("weather: {} {:.2f}".format(weatherCondition, temperature))

for i in range(10):
    test()
