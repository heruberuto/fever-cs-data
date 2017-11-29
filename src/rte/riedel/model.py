from torch import nn

class SimpleMLP(nn.Module):
    def __init__(self,input_dim,hidden_dim,output_dim,dropout_p=.6):
        super(SimpleMLP, self).__init__()
        self.fc1 = nn.Linear(input_dim,hidden_dim)
        self.fc2 = nn.Linear(hidden_dim,output_dim)

        self.do = nn.Dropout(dropout_p)
        self.relu = nn.ReLU()

    def forward(self,x):
        x = self.do(x)
        x = self.fc1(x)

        x = self.relu(x)

        x = self.do(x)
        x = self.fc2(x)

        return x





